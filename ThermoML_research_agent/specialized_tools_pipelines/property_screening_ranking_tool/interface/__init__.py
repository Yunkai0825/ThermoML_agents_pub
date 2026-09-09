"""Public request contracts.

Query-agent adapters live in :mod:`interface.agent` so importing the
scientific pipeline does not register agent hooks as a side effect.
"""
from .models import (
    BaselineKind,
    CandidateRef,
    ConstraintSpec,
    Diagnostic,
    DiscoveryResult,
    GridPoint,
    InterpolatedCriterion,
    NormalizedRequest,
    RankingTarget,
    SourceSeries,
)
from .request import (
    RequestReviewOutcome,
    RequestValidationError,
    parse_request,
    review_request,
)

__all__ = [
    "BaselineKind",
    "CandidateRef",
    "ConstraintSpec",
    "Diagnostic",
    "DiscoveryResult",
    "GridPoint",
    "InterpolatedCriterion",
    "NormalizedRequest",
    "RankingTarget",
    "RequestReviewOutcome",
    "RequestValidationError",
    "SourceSeries",
    "parse_request",
    "review_request",
]
