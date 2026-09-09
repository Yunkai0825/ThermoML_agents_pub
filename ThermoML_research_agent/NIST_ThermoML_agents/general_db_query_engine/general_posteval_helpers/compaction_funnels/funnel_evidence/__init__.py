"""Evidence layer — logged-first session parsing (exhaustive logs only).

Sizes come from the logs (pipeline table authoritative); pre-delivery
text/ids come from re-execution FROM VERBATIM LOGGED ARGS only
(funnel_evidence.reexec).  Legacy sessions raise LegacySessionError.
"""

from funnel_evidence.measures import (  # noqa: F401
    Measure, measure, thermoml_ids, block_tokens, qualified_block_pts,
    build_block_canon,
)
from funnel_evidence.history_evidence import (  # noqa: F401
    LegacySessionError, SessionHistory, Step, PipelineRow, SubagentRow,
    session_history, is_exhaustive,
)
from funnel_evidence.stats_evidence import (  # noqa: F401
    ArgoRow, ToolRow, argo_rows, tool_rows, run_window,
)
from funnel_evidence.event_evidence import (  # noqa: F401
    Event, events, verbatim_output, triage_events, turn_events,
)
from funnel_evidence.envelope_evidence import (  # noqa: F401
    EnvelopePartition, envelope_partition, envelope_blob, ledger_section,
)
from funnel_evidence.memory_evidence import (  # noqa: F401
    WmRecord, wm_records, wm_measure, wm_path, context_ids,
)
from funnel_evidence.reexec import reexec_stages  # noqa: F401
from funnel_evidence.delegation_tree import (  # noqa: F401
    AgentInstance, DelegationTree, ToolUse, build_tree,
)
