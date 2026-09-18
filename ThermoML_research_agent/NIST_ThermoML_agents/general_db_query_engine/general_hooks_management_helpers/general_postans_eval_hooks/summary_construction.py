"""Hidden summary constructor for ThermoML post-answer ID alignment."""

from __future__ import annotations

from typing import Any

from ...general_tool_management_helpers.general_agent_tool_catalog import (
    AgentToolCatalog,
    ToolEntry,
)
from ...general_argo_engine_helpers.json_answer_guard import guard_json_answer


SUMMARY_SCHEMA = {"summary": "Concise summary of the completed answer."}

_SUMMARY_SYSTEM = """
You are the answer-summary constructor inside the ThermoML ID-alignment
post-answer stage. You have no database or search tools. Read only the
completed chemistry answer and compress its main result, scope, and decisive
qualification into a concise summary.

Do not add claims, identifiers, evidence, metadata, or conclusions that are
not stated in the answer. Reproduce any numbers VERBATIM from the answer —
omit a number rather than approximate it. Do not produce a core_claims
array. Output exactly one JSON object with one field named `summary`, whose
value is non-empty text. No prose, tags, code fences, or extra fields.
""".strip()


def construct_answer_summary(
    answer: str,
    *,
    client: Any,
    label: str,
    max_retries: int = 1,
    max_tokens: int = 1000,
) -> dict[str, str]:
    """Construct the final ``summary`` from the answer and nothing else."""
    if not isinstance(answer, str) or not answer.strip():
        raise ValueError("answer must be non-empty text")
    raw = client.call(
        "## Completed chemistry answer\n" + answer.strip(),
        _SUMMARY_SYSTEM,
        max_tokens=max_tokens,
    )
    parsed, _ = guard_json_answer(
        raw,
        client=client,
        label=f"{label}-postanswer-summary",
        schema=SUMMARY_SCHEMA,
        max_retries=max_retries,
        max_tokens=max_tokens,
    )
    if not isinstance(parsed, dict) or set(parsed) != {"summary"}:
        raise ValueError("summary constructor must return exactly summary")
    summary = parsed["summary"]
    if not isinstance(summary, str) or not summary.strip():
        raise TypeError("summary constructor must return non-empty text")
    return {"summary": summary.strip()}


class SummaryConstructionToolCatalog(AgentToolCatalog):
    """The one hidden tool owned by the ID-alignment branch."""

    pipeline_label = "postanswer-summary"

    def __init__(self) -> None:
        super().__init__(
            entries=(
                ToolEntry(
                    "construct_answer_summary",
                    construct_answer_summary,
                    group="id_alignment_construction",
                    skip_compactor=True,
                    skip_subagent=True,
                ),
            )
        )


SUMMARY_CONSTRUCTION_TOOL_CATALOG = SummaryConstructionToolCatalog()


__all__ = [
    "SUMMARY_SCHEMA",
    "construct_answer_summary",
    "SummaryConstructionToolCatalog",
    "SUMMARY_CONSTRUCTION_TOOL_CATALOG",
]
