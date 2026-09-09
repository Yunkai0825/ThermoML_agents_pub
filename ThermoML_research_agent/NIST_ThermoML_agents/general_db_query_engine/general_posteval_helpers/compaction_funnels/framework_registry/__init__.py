"""Central framework registry for the compaction funnels.

Single source of truth for the agent/tool hierarchy of the ThermoML
multi-agent framework, verified against the live catalogs on
2026-08-15 (see DEBUG_scripts/_introspect_catalogs snapshot):

- tool_registry   — every tool: owning catalog, compaction flags,
                    dispatch target, inspection/fit-rail markers.
- agent_registry  — every agent layer: callable tools, dispatchable
                    subagents, envelope schema (field provenance
                    classes), gate config, support-context sources.
- stage_templates — the Sankey block grammar: roles, support classes,
                    sink families, block factories with stable keys +
                    agentic/pooled merge group keys.

Parenthood in sessions is TYPE-AGNOSTIC: an instance's parent is
whichever instance actually dispatched it (Main can parent a Q_L1 via
the menu; A_L0 parents Q_L1 in-process; Q_L1 parents L2_*).  The
registry only declares what CAN happen; the delegation tree records
what DID happen.
"""

from .tool_registry import (  # noqa: F401
    ToolSpec,
    TOOLS,
    SUBSTEP_KEYS,
    MENU_WRAPPER,
    MENU_PLANNER,
    tool_spec,
    chain_shape,
    FULL_PIPELINE,
    DET_ONLY,
    EXEMPT,
    RELAY,
)
from .agent_registry import (  # noqa: F401
    AgentSpec,
    AGENTS,
    FieldClass,
    agent_for_dispatcher,
    agent_spec,
)
from .stage_templates import (  # noqa: F401
    NodeRole,
    SupportClass,
    SinkFamily,
    BlockSpec,
    tool_stage_block,
    tool_family,
    context_block,
    answer_block,
    envelope_part_block,
    deliverable_block,
    wrapper_block,
    support_block,
    wm_archive_block,
    introduced_block,
    hydration_block,
    expansion_block,
    sink_block,
    batch_block,
    validate_registry,
)
