#!/usr/bin/env python
"""Rebuild the regression fixtures through the public API.

    python -B DEBUG_runner.py debug            # all six fixtures
    python -B DEBUG_runner.py debug --no-render  # TSVs + audits only

Outputs land in _benchmark/Main/Diagnostics/compaction_funnels/<label>/
at the workspace root (fixture session dirs stay untouched).  Exit code 1 on any audit FAIL or generation error.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_PACKAGE_ROOT = Path(__file__).resolve().parent
if str(_PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_PACKAGE_ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("families", nargs="*", default=["debug"],
                        choices=["debug"],
                        help="only the fixture regression remains")
    parser.add_argument("--no-render", action="store_true",
                        help="skip figure rendering (TSVs + audits only)")
    args = parser.parse_args()

    from api import generate_workflow
    from run_library.fixtures import DEBUG_OUTPUT, FIXTURES

    failures = 0
    for label, session, kind in FIXTURES:
        out_dir = DEBUG_OUTPUT / label
        print(f"\n=== {label} ({kind}) ===")
        if not session.exists():
            print(f"  MISSING fixture session: {session}")
            failures += 1
            continue
        if args.no_render:
            from funnel_assembly.build import build_all
            from workflow_audits.registry_audits import (run_audits,
                                                         write_report)
            result = build_all(session, kind, label, out_dir, render=False)
            findings = run_audits(result)
            write_report(findings, out_dir / "registry_audit_report.tsv")
            n_fail = sum(1 for f in findings if f.severity == "FAIL")
            print(f"  outputs={len(result['outputs'])} findings="
                  f"{len(findings)} FAIL={n_fail}")
            failures += n_fail
        else:
            report = generate_workflow(session, kind=kind, label=label,
                                       out_dir=out_dir)
            status = "ok" if report.ok else f"ERROR: {report.error}"
            print(f"  {status} outputs={len(report.outputs)} findings="
                  f"{report.audit_findings} FAIL={report.audit_failures} "
                  f"({report.elapsed_seconds:.1f}s)")
            failures += report.audit_failures + (0 if report.ok else 1)
    print(f"\ntotal audit failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
