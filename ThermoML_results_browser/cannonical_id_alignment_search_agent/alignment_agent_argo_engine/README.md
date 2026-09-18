# Alignment Agent — Argo Engine

Argo LLM ReAct client for the alignment agent.

## Files

| File | Purpose |
|------|---------|
| `argo_client.py` | `AlignmentClient` — subclass of `ArgoClient` |
| `__init__.py` | Package init |

## AlignmentClient

Extends the shared `ArgoClient` base class with alignment-specific
configuration (model, system prompt, tool catalog).

```python
client = AlignmentClient.for_l0()
```

Factory method `for_l0()` wires up:
- Model / temperature from `alignment_agent_argo_config`
- Tool catalog from `alignment_agent_toolbox`
- L0 orchestrator workflow
