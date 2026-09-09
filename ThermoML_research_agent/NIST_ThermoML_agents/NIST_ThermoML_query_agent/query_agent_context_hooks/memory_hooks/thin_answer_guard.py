"""Post-loop guard: detect chatbot-style "thin" answers and force data.

When the L0 agent stores data in working memory but gives back only a
chatbot-style acknowledgement ("saved to memory", "anything else?"),
this guard re-prompts the LLM to include the actual data.

Usage::

    from ..memory_hooks.thin_answer_guard import (
        is_thin_answer, force_data_presentation,
    )

    if is_thin_answer(result.answer, saver.call_count):
        result = force_data_presentation(
            result, mem_tools, memory, client, system_prompt,
        )
"""

from __future__ import annotations

import logging

from ....general_db_query_engine.general_argo_engine_helpers.engine_react_helpers.react_helpers import AgentTurnResult
from ....general_db_query_engine.general_argo_engine_helpers.engine_react_helpers.react_loop import _clean_answer_text

log = logging.getLogger("L0-Orchestrator")

THIN_MARKERS = [
    "stored in memory", "saved to memory", "anything else",
    "would you like", "is there anything", "confirmation is noted",
    "has been saved", "has been stored", "let me know",
    "stored in working memory", "thank you for confirming",
]


def is_thin_answer(answer: str, l1_call_count: int) -> bool:
    """Return *True* when the answer reads like a stub instead of real data.

    The heuristic fires when at least one L1 query was executed (so data
    *should* exist) and the answer contains multiple chatbot filler phrases
    or is very short with even one marker.
    """
    if l1_call_count < 1:
        return False
    answer_lower = answer.lower()
    marker_count = sum(1 for m in THIN_MARKERS if m in answer_lower)
    return (
        marker_count >= 2
        or (len(answer) < 300 and marker_count >= 1)
    )


def force_data_presentation(
    result,          # AgentTurnResult (imported lazily to avoid circular refs)
    mem_tools,
    memory: list[dict],
    client,
    system_prompt: str,
):
    """Re-prompt the LLM to include actual data from working memory.

    Returns a new ``AgentTurnResult`` with the enriched answer, or the
    original *result* unchanged if the Results section is empty.
    """
    wm_content = mem_tools.memory_read("Results")
    if not wm_content or len(wm_content.strip()) <= 50:
        return result

    log.warning("Thin answer detected — forcing data presentation")
    followup_prompt = (
        "Your previous answer was too brief and did not include the "
        "actual data.  The user CANNOT see your working memory.\n\n"
        "Here is what was stored in Results:\n"
        f"{wm_content[:3000]}\n\n"
        "Now rewrite your answer to include ALL the key data, numbers, "
        "DOIs, property lists, temperature ranges, and block counts "
        "from the above.  Present it directly — do not reference "
        "'working memory' or say 'stored'.  Be comprehensive."
    )
    memory.append({"role": "user", "content": followup_prompt})
    final = client.call(
        "\n\n".join(
            f"## {'User' if t['role'] == 'user' else 'Assistant'}\n{t['content']}"
            for t in memory
        ),
        system_prompt,
    )
    memory.append({"role": "assistant", "content": final})
    return AgentTurnResult(
        answer=_clean_answer_text(final),
        iterations=result.iterations + 1,
        elapsed_seconds=result.elapsed_seconds,
        tool_history=result.tool_history,
        timed_out=result.timed_out,
    )
