"""
Clean up raw LLM answers for display.
======================================
Strips tool-call XML, echoed conversation turns, and bare JSON artefacts
from the final answer text before writing to result files.
"""
from __future__ import annotations

import re

_TOOL_XML_RE = re.compile(
    r"<tool_(?:call|result)>.*?</tool_(?:call|result)>", re.DOTALL,
)


def clean_answer(raw: str) -> str:
    """Strip tool XML and echoed conversation turns from the final answer."""
    text = _TOOL_XML_RE.sub("", raw)
    parts = re.split(r"(?=^## (?:User|Assistant))", text, flags=re.MULTILINE)
    cleaned = []
    for p in parts:
        if p.startswith("## User"):
            continue
        if p.startswith("## Assistant"):
            p = re.sub(r"^## Assistant\n", "", p)
        cleaned.append(p)
    text = "\n".join(cleaned)
    text = re.sub(r"\n{4,}", "\n\n\n", text).strip()
    if not text:
        raise ValueError(
            "FINAL_ANSWER_SCHEMA_ERROR: model output contained no displayable final answer"
        )
    return text
