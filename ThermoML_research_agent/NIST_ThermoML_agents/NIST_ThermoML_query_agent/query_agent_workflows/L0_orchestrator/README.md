# L0 Orchestrator

Entry point for the ThermoML query agent system.

## Files

| File | Purpose |
|------|---------|
| `orchestrator.py` | `run()` — main entry point; loads L0 workflow, wires tools, drives ReAct loop |
| `L0_orchestrator_workflow.md` | System prompt, tool catalog, prompt template, output schema, 4 phases |

## How It Works

```
run(user_question, memory_path=None)
    │
    ├─ parse_workflow(L0_orchestrator_workflow.md)
    ├─ WorkingMemory.init(path)
    ├─ Build tool registry:
    │     memory_read         → memory_management_MCP_tools
    │     memory_append_history → ...
    │     memory_add_result   → ...
    │     memory_catalog_add  → ...
    │     memory_catalog_remove → ...
    │     memory_catalog_list → ...
    │     L1_query            → _l1_query_with_autosave(dispatch_l1_query)
    │
    ├─ agent_turn(client_L0, system_prompt, tools, ...)
    │     └─ ReAct loop: LLM → tool_call → execute → repeat
    │
    ├─ Thin-answer guard (forces data presentation if chatbot-style response)
    │
    └─ Returns AgentTurnResult(answer, history, memory_snapshot)
```

## Key Design Decisions

1. **Auto-save L1 results**: `_l1_query_with_autosave()` wraps every L1 dispatch
   to automatically store results in Working Memory. The LLM is not relied on
   to remember to call `memory_add_result` (it often doesn't).

2. **Thin-answer guard**: After the agent loop completes, if the answer matches
   chatbot markers ("stored in memory", "let me know", etc.) a forced follow-up
   call extracts the actual data from the Results section.

3. **Memory injection**: Working Memory content is prepended to every LLM call
   as a preamble, outside the conversation memory list.

## Workflow Phases

| Phase | Name | Tools | Purpose |
|-------|------|-------|---------|
| 1 | `understand_and_plan` | memory_tools | Parse question, populate ID Catalog |
| 2 | `dispatch_query` | L1_query, memory_tools | Send structured purpose+instruction to L1 |
| 3 | `review_and_iterate` | memory_tools, L1_query | Check if answer is complete, iterate if needed |
| 4 | `formulate_answer` | memory_tools | Read memory → generate final answer |
