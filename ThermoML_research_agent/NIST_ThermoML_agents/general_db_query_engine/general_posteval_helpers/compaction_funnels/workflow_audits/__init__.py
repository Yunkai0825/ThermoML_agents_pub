"""Registry-driven audits over built funnel skeletons.

Single module ``registry_audits`` — runs on the in-memory build result
(skeletons + projected graphs + delegation tree), not on re-parsed
TSVs:

- conservation: per-node in/out balance for every identity (chars sum,
  ids/blocks set containment, pts weights) at every level.
- adjacency: every edge legal under the stage-template grammar
  (role-to-role transitions declared in ``framework_registry``).
- coverage: logged evidence universe (pipeline stages ∪ envelope ∪
  ledger ids) ⊆ detailed ids graph.
- envelope partition: Σ envelope part chars == result.md envelope
  bytes; ledger == "## Data Inspections" section.
- reexec drift: re-executed stage sizes vs the logged pipeline table
  (WARN — "DB changed since run").

Report: ``registry_audit_report.tsv`` (severity FAIL/WARN/INFO).
Wired automatically by ``api.generate_workflow``; standalone via
``DEBUG_runner.py debug --no-render``.
"""
