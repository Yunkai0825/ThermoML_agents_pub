"""
Review workers — field-specific agents that refine search fields.

After the alignment agent fills fields and the validator flags issues,
review workers examine the top search results and suggest field edits.

Worker types
------------
- **LiteratureReviewWorker**: examines title hits, extracts compound
  and property mentions from titles, suggests field corrections.
- **CompoundReviewWorker**: cross-checks compound names against the
  compound registry and suggests canonical alternatives.
- **PropertyReviewWorker**: checks property keywords against the
  property registry and suggests refined terms.

Each worker is stateless: takes current fields + top results → returns
a list of ``FieldEdit`` suggestions.

Escalation
----------
If workers cannot resolve ambiguity (e.g. all suggestions score < 50),
the dispatcher marks the query for escalation to the ThermoML query
agent, which uses LLM reasoning to interpret the intent.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

from .id_workers import (
    ResolvedID,
    resolve_compound,
    resolve_property,
    resolve_measurement,
)
from .bibliography_scorer import TitleHit, score_titles, _tokenise


# ── Data classes ──────────────────────────────────────────────────────────

@dataclass
class FieldEdit:
    """A suggested edit to a search field."""
    field_name: str           # e.g. "compound", "property", "title_keywords"
    action: str               # "replace", "add", "remove", "refine"
    old_value: str
    new_value: str
    reason: str
    confidence: int           # 0-100
    source: str               # which worker suggested this

    def to_dict(self) -> dict:
        return {
            "field_name": self.field_name,
            "action": self.action,
            "old_value": self.old_value,
            "new_value": self.new_value,
            "reason": self.reason,
            "confidence": self.confidence,
            "source": self.source,
        }


@dataclass
class ReviewResult:
    """Output from a review worker."""
    worker_name: str
    edits: list[FieldEdit] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    needs_escalation: bool = False
    escalation_reason: str = ""

    def to_dict(self) -> dict:
        return {
            "worker_name": self.worker_name,
            "edits": [e.to_dict() for e in self.edits],
            "notes": self.notes,
            "needs_escalation": self.needs_escalation,
            "escalation_reason": self.escalation_reason,
        }


# ── Literature Review Worker ──────────────────────────────────────────────

# Patterns to extract compound-like phrases from titles
_COMPOUND_PATTERN = re.compile(
    r'\b(?:aqueous|binary|ternary)\s+(?:mixtures?\s+of\s+)?'
    r'([A-Z][a-z]*(?:\s+[A-Z][a-z]*)*)',
    re.IGNORECASE
)

# Common property words found in titles
_TITLE_PROP_KEYWORDS = {
    "density", "viscosity", "conductivity", "refractive",
    "heat capacity", "enthalpy", "entropy", "surface tension",
    "speed of sound", "solubility", "diffusion", "osmotic",
    "vapor pressure", "boiling", "melting", "critical",
    "compressibility", "permittivity", "excess",
}


def review_literature(title_hits: list[TitleHit],
                      current_compounds: list[str],
                      current_properties: list[str]) -> ReviewResult:
    """Review top title hits and suggest field edits.

    Extracts compound and property mentions from high-scoring titles,
    compares with current field values, and suggests additions/replacements.
    """
    result = ReviewResult(worker_name="LiteratureReviewWorker")

    if not title_hits:
        result.notes.append("No title hits to review")
        return result

    # Collect compound and property mentions from top titles
    compound_mentions: dict[str, int] = {}   # name → count
    property_mentions: dict[str, int] = {}

    for hit in title_hits[:15]:  # review top 15
        title_lower = hit.title.lower()

        # Extract compound-like names from title
        # Look for capitalized multi-word phrases (likely compound names)
        # Split on common separators
        for segment in re.split(r'\s+(?:and|with|in|of|for)\s+', hit.title):
            segment = segment.strip()
            # Check if this segment resolves as a compound
            if len(segment) > 2 and not segment[0].isdigit():
                tokens = _tokenise(segment)
                for tok in tokens:
                    if len(tok) > 3:  # skip very short words
                        hits = resolve_compound(tok, limit=1)
                        if hits and hits[0].score >= 70:
                            name = hits[0].display_name
                            compound_mentions[name] = compound_mentions.get(name, 0) + 1

        # Extract property keywords from titles
        for prop_kw in _TITLE_PROP_KEYWORDS:
            if prop_kw in title_lower:
                property_mentions[prop_kw] = property_mentions.get(prop_kw, 0) + 1

    # Compare with current fields and suggest edits
    current_comp_lower = {c.lower() for c in current_compounds}
    current_prop_lower = {p.lower() for p in current_properties}

    # Suggest new compounds found in titles but not in current fields
    for name, count in sorted(compound_mentions.items(), key=lambda x: -x[1]):
        if count >= 2 and name.lower() not in current_comp_lower:
            result.edits.append(FieldEdit(
                field_name="compound",
                action="add",
                old_value="",
                new_value=name,
                reason=f"Found in {count} top-scoring titles",
                confidence=min(85, 50 + count * 10),
                source="LiteratureReviewWorker",
            ))

    # Suggest property refinements
    for prop_kw, count in sorted(property_mentions.items(), key=lambda x: -x[1]):
        if count >= 3 and prop_kw not in current_prop_lower:
            result.edits.append(FieldEdit(
                field_name="property",
                action="add",
                old_value="",
                new_value=prop_kw,
                reason=f"Mentioned in {count} top-scoring titles",
                confidence=min(80, 40 + count * 10),
                source="LiteratureReviewWorker",
            ))

    if not result.edits:
        result.notes.append("Literature review: current fields align well with top titles")

    return result


# ── Compound Review Worker ────────────────────────────────────────────────

def review_compounds(compounds: list[ResolvedID],
                     unresolved: list[str]) -> ReviewResult:
    """Review compound resolutions and suggest corrections.

    For each resolved compound, re-checks against the registry.
    For unresolved tokens, attempts compound resolution.
    """
    result = ReviewResult(worker_name="CompoundReviewWorker")

    for comp in compounds:
        if comp.score < 70:
            # Try re-resolving with relaxed threshold
            hits = resolve_compound(comp.display_name, limit=5)
            if hits and hits[0].score > comp.score:
                result.edits.append(FieldEdit(
                    field_name="compound",
                    action="replace",
                    old_value=comp.display_name,
                    new_value=hits[0].display_name,
                    reason=(
                        f"Better match found: {hits[0].display_name} "
                        f"(score {hits[0].score} vs {comp.score})"
                    ),
                    confidence=hits[0].score,
                    source="CompoundReviewWorker",
                ))

    # Try resolving unresolved tokens as compounds
    for token in unresolved:
        if token.startswith(("prop:", "meas:", "var:", "constr:")):
            continue  # skip typed failures
        hits = resolve_compound(token, limit=3)
        if hits and hits[0].score >= 60:
            result.edits.append(FieldEdit(
                field_name="compound",
                action="add",
                old_value=token,
                new_value=hits[0].display_name,
                reason=f"Unresolved '{token}' matches compound '{hits[0].display_name}' (score={hits[0].score})",
                confidence=hits[0].score,
                source="CompoundReviewWorker",
            ))
        elif not hits or hits[0].score < 40:
            result.needs_escalation = True
            result.escalation_reason = (
                f"Cannot resolve '{token}' as a compound (best score: "
                f"{hits[0].score if hits else 0}). Needs query agent."
            )

    return result


# ── Property Review Worker ────────────────────────────────────────────────

def review_properties(properties: list[ResolvedID],
                      unresolved: list[str]) -> ReviewResult:
    """Review property resolutions and suggest corrections."""
    result = ReviewResult(worker_name="PropertyReviewWorker")

    for prop in properties:
        if prop.score < 70:
            hits = resolve_property(prop.display_name, limit=5)
            if hits and hits[0].score > prop.score:
                result.edits.append(FieldEdit(
                    field_name="property",
                    action="replace",
                    old_value=prop.display_name,
                    new_value=hits[0].display_name,
                    reason=(
                        f"Better match: {hits[0].display_name} "
                        f"(score {hits[0].score} vs {prop.score})"
                    ),
                    confidence=hits[0].score,
                    source="PropertyReviewWorker",
                ))

    for token in unresolved:
        if not token.startswith("prop:"):
            continue
        name = token.split(":", 1)[1]
        hits = resolve_property(name, limit=3)
        if hits and hits[0].score >= 50:
            result.edits.append(FieldEdit(
                field_name="property",
                action="add",
                old_value=token,
                new_value=hits[0].display_name,
                reason=f"Re-resolved '{name}' → '{hits[0].display_name}' (score={hits[0].score})",
                confidence=hits[0].score,
                source="PropertyReviewWorker",
            ))

    # Also try measurements for unresolved prop tokens
    for token in unresolved:
        if not token.startswith("meas:"):
            continue
        name = token.split(":", 1)[1]
        hits = resolve_measurement(name, limit=3)
        if hits and hits[0].score >= 50:
            result.edits.append(FieldEdit(
                field_name="measurement",
                action="add",
                old_value=token,
                new_value=hits[0].display_name,
                reason=f"Re-resolved '{name}' → '{hits[0].display_name}' (score={hits[0].score})",
                confidence=hits[0].score,
                source="PropertyReviewWorker",
            ))

    return result


# ── Orchestrate all workers ───────────────────────────────────────────────

def run_all_workers(resolved_query,
                    title_hits: list[TitleHit] | None = None,
                    db_path: str = "") -> list[ReviewResult]:
    """Run all review workers on a ResolvedQuery.

    Parameters
    ----------
    resolved_query : ResolvedQuery
        The dispatcher's output.
    title_hits : list[TitleHit], optional
        Pre-computed title hits for literature review.
    db_path : str
        Path to ThermoML_index.db.

    Returns
    -------
    list[ReviewResult]
        One ReviewResult per worker.
    """
    results = []

    # Literature review (if title keywords exist)
    if title_hits or resolved_query.title_words:
        if not title_hits and db_path:
            kw = " ".join(resolved_query.title_words)
            title_hits = score_titles(kw, db_path, limit=15)
        if title_hits:
            comp_names = [c.display_name for c in resolved_query.compounds]
            prop_names = [p.display_name for p in resolved_query.properties]
            results.append(review_literature(title_hits, comp_names, prop_names))

    # Compound review
    results.append(review_compounds(
        resolved_query.compounds,
        resolved_query.unresolved,
    ))

    # Property review
    results.append(review_properties(
        resolved_query.properties,
        resolved_query.unresolved,
    ))

    return results


def apply_edits(resolved_query, edits: list[FieldEdit],
                min_confidence: int = 60) -> list[str]:
    """Apply accepted FieldEdits to a ResolvedQuery in place.

    Only applies edits with confidence >= min_confidence.
    Returns a log of applied changes.
    """
    log = []

    for edit in edits:
        if edit.confidence < min_confidence:
            continue

        if edit.field_name == "compound" and edit.action == "add":
            hits = resolve_compound(edit.new_value, limit=1)
            if hits:
                resolved_query.compounds.append(hits[0])
                log.append(f"Added compound: {hits[0].display_name}")

        elif edit.field_name == "compound" and edit.action == "replace":
            for i, comp in enumerate(resolved_query.compounds):
                if comp.display_name == edit.old_value:
                    hits = resolve_compound(edit.new_value, limit=1)
                    if hits:
                        resolved_query.compounds[i] = hits[0]
                        log.append(
                            f"Replaced compound: {edit.old_value} → {hits[0].display_name}"
                        )
                    break

        elif edit.field_name == "property" and edit.action in ("add", "replace"):
            hits = resolve_property(edit.new_value, limit=1)
            if hits:
                if edit.action == "add":
                    resolved_query.properties.append(hits[0])
                    log.append(f"Added property: {hits[0].display_name}")
                else:
                    for i, prop in enumerate(resolved_query.properties):
                        if prop.display_name == edit.old_value:
                            resolved_query.properties[i] = hits[0]
                            log.append(
                                f"Replaced property: {edit.old_value} → {hits[0].display_name}"
                            )
                            break

        elif edit.field_name == "measurement" and edit.action == "add":
            hits = resolve_measurement(edit.new_value, limit=1)
            if hits:
                resolved_query.measurements.append(hits[0])
                log.append(f"Added measurement: {hits[0].display_name}")

    return log
