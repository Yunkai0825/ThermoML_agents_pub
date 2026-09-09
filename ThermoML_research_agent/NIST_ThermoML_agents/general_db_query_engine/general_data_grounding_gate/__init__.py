"""Mandatory data-grounding gate + verbatim inspection registry (v4 workflow).

Public surface for the react loop, post-answer assembly, and dispatchers.
"""

from .inspection_harvest import (
    INSPECT_TOOL_NAME,
    entry_from_structured,
    export_inspections,
    harvest_fit_artifacts,
    harvest_inspection_targets,
    harvest_inspections,
    parse_inspection_markdown,
)
from .authoritative_blocks import default_authoritative_fetch
from .evidence_log import build_evidence_log, write_grounding_evidence
from .grounding_gate import (
    FLAGS_HEADER,
    GATE_MARKER,
    MAX_GATE_BOUNCES,
    GateReport,
    build_flags_note,
    build_gate_nudge,
    build_grounded_context,
    build_timeout_gate_instruction,
    build_violation_report,
    count_gate_bounces,
    gate_enabled,
    run_data_grounding_gate,
)

__all__ = [
    "INSPECT_TOOL_NAME",
    "entry_from_structured",
    "export_inspections",
    "harvest_fit_artifacts",
    "harvest_inspection_targets",
    "harvest_inspections",
    "parse_inspection_markdown",
    "default_authoritative_fetch",
    "build_evidence_log",
    "write_grounding_evidence",
    "FLAGS_HEADER",
    "GATE_MARKER",
    "MAX_GATE_BOUNCES",
    "GateReport",
    "build_flags_note",
    "build_gate_nudge",
    "build_grounded_context",
    "build_timeout_gate_instruction",
    "build_violation_report",
    "count_gate_bounces",
    "gate_enabled",
    "run_data_grounding_gate",
]
