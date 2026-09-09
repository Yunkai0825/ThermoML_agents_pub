"""
Argo API configuration for the Canonical ID Alignment Search Agent.
==================================================================
Lightweight agent config — runs with fewer iterations and shorter
timeouts than the full query agent since its task is narrowly scoped:
resolve search terms → canonical IDs → validate → fill fields.

This agent does NOT need L1/L2 sub-agents; it operates as a single
ReAct loop calling MCP tools directly.
"""

import os
from dataclasses import dataclass, field

from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers.engine_config import EngineConfig


def _default_api_user() -> str:
    """Read the account configured for the Argo provider."""
    return os.environ.get("ARGO_API_USER", "").strip()


@dataclass
class AlignmentAgentConfig(EngineConfig):
    """Configuration for the canonical ID alignment search agent.

    Inherits all 26 EngineConfig fields + agent-specific fields.
    Deliberately lighter than the query agent: fewer iterations,
    shorter timeout, smaller token budget.
    """

    # ═══════════════════════════════════════════════════════════
    # Step 1 — Engine config fields (consumed by argo_engine_helpers)
    # ═══════════════════════════════════════════════════════════

    # ── API connection ──────────────────────────────────────
    API_URL: str = "https://apps-dev.inside.anl.gov/argoapi/api/v1/resource/chat/"
    API_USER: str = field(default_factory=_default_api_user)
    HEADERS: dict = field(default_factory=lambda: {"Content-Type": "application/json"})

    # ── Model names ─────────────────────────────────────────
    MODEL: str = "claudeopus46"           # Primary model
    VERDICT_MODEL: str = "claudeopus46"   # Post-job reviewer
    PLANNER_MODEL: str = "claudeopus46"   # Strategy planner

    # ── Generation parameters ───────────────────────────────
    TEMPERATURE: float = 0.2    # Low temperature for deterministic ID matching
    TOP_P: float = 0.9
    MAX_TOKENS: int = 4000      # Smaller than query agent (no long narratives)
    HTTP_TIMEOUT: int = 300     # 5 min max per API call

    # ── Agent loop limits (L0) ──────────────────────────────
    MAX_TOOL_ITERATIONS: int = 15   # Fewer iterations — task is focused
    MAX_TURN_SECONDS: int = 300     # 5 min wall-clock budget

    # ── L2 async limits ─────────────────────────────────────
    L2_MAX_ITERATIONS: int = 4    # Lightweight L2 if needed
    L2_MAX_SECONDS: int = 60

    # ── Time warnings ───────────────────────────────────────
    WARN_THRESHOLDS: list[float] = field(default_factory=lambda: [0.65, 0.85, 0.95])
    MAX_WRAP_WARNINGS: int = 2
    MAX_EMPTY_WAITS: int = 2

    # ── Tool result truncation ──────────────────────────────
    TOOL_RESULT_CHAR_LIMIT: int = 16_000

    # ── Compaction ──────────────────────────────────────────
    COMPACTION_TRIGGER_CHARS: int = 40_000
    SUMMARY_MAX_CHARS: int = 800
    GUIDANCE_MAX_TOKENS: int = 100

    # ── Deterministic stage compaction ─────────────────────
    # Required by the shared ReAct loop when one agent turn batches several
    # tool results.  Alignment results are already compact native objects, so
    # retain a modest but non-truncating stage budget.
    STAGE_COMPACT_BUDGET: int = 8_000
    STAGE_NOTE_CHARS: int = 200

    # ── Full-context interactive compaction ────────────────
    # The standalone alignment agent uses the shared ReAct loop without a
    # custom hook bundle, so its config must provide the complete contract
    # consumed by ``compact_memory``.
    KEEP_RECENT_RESULTS: int = 2
    MIN_COMPRESS_CHARS: int = 500
    COMPRESS_SHORT_THRESHOLD: int = 1_500
    MAX_RETRY: int = 5
    MAX_IMMEDIATE_RETRY: int = 2
    COMPRESS_MAX_WORDS: int = 500
    COMPRESS_SUMMARY_CHARS: int = 800

    # ── Verdict / Compactor / Planner ───────────────────────
    VERDICT_TEMPERATURE: float = 0.1
    VERDICT_MAX_TOKENS: int = 400
    COMPACTOR_TEMPERATURE: float = 0.1
    COMPACTOR_MAX_TOKENS: int = 800
    PLANNER_TEMPERATURE: float = 0.2
    PLANNER_MAX_TOKENS: int = 600

    # ═══════════════════════════════════════════════════════════
    # Step 2 — Alignment-agent-specific fields
    # ═══════════════════════════════════════════════════════════

    # Validation thresholds
    VALIDATION_PASS_SCORE: int = 80     # Score >= this → field passes
    VALIDATION_WARN_SCORE: int = 50     # Score 50-79 → ambiguous warning
    AUTO_APPLY_MIN_CONFIDENCE: int = 60 # Min confidence for auto-applying edits

    # Escalation settings
    ESCALATION_ENABLED: bool = False    # Default: no query agent escalation
    ESCALATION_TIMEOUT: int = 120       # Max seconds for query agent call


AGENT_CONFIG = AlignmentAgentConfig()
