#!/usr/bin/env python
"""
ThermoML Analysis Agent — Test Runner (sequential + parallel)
==============================================================
Thin wrapper around shared test-runner helpers.  Agent-specific logic
is limited to ``run_one_prompt()`` which calls the analysis orchestrator.

Usage:
    python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests
    python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests 1.1 2.1
    python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests --section 2
    python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests --workers 5 --gap 6
"""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import sys
import time
from dataclasses import asdict
from pathlib import Path

_THIS_DIR = Path(__file__).absolute().parent
_AGENT_DIR  = _THIS_DIR.parent                  # NIST_ThermoML_analysis_agent
_AGENTS_DIR = _AGENT_DIR.parent                  # NIST_ThermoML_agents
_WORKSPACE  = _AGENTS_DIR.parent                 # ThermoML_research_agent
for p in (_THIS_DIR, _WORKSPACE):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-5s | %(name)-18s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("ANALYSIS-TEST")

_BENCHMARK_ROOT = _WORKSPACE.parent / "_benchmark" / "Analysis"

# ── Shared helpers ──────────────────────────────────────────────────────────
from NIST_ThermoML_agents.general_db_query_engine.general_DEBUG_test_runner_helpers import (
    parse_prompts_simple,
    run_sequential,
    run_parallel,
    setup_run_log,
    teardown_run_log,
)
from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_tracking_hooks_output_helpers import (
    get_status,
    write_result_md,
    write_history_md,
    write_summary_md,
    write_json_trace,
)
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_analysis_api import ThermoML_analysis_run


# ═══════════════════════════════════════════════════════════════
#  Run one prompt  (agent-specific)
# ═══════════════════════════════════════════════════════════════

def run_one_prompt(pid: str, prompt: str, output_dir: Path) -> dict:
    """Run a single prompt and return a standardised result dict."""
    log.info(">>> Running %s: %s", pid, prompt[:80])
    t0 = time.time()
    try:
        raw_result = ThermoML_analysis_run(
            prompt, run_verdict=True, session_dir=output_dir / f"Q{pid}",
        )
        result = asdict(raw_result) if hasattr(raw_result, '__dataclass_fields__') else dict(raw_result)
    except Exception as e:
        log.error("FAILED %s: %s", pid, e, exc_info=True)
        result = {
            "answer": f"ERROR: {e}",
            "verdict": None,
            "iterations": 0,
            "elapsed_seconds": time.time() - t0,
            "tool_history": [],
            "timed_out": False,
        }

    # Normalise to standard keys expected by shared writers
    result["prompt_id"] = pid
    result["prompt_text"] = prompt
    if "elapsed_seconds" in result and "elapsed_s" not in result:
        result["elapsed_s"] = round(result.pop("elapsed_seconds"), 1)

    return result


# ═══════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="ThermoML Analysis Agent Test Runner")
    parser.add_argument("ids", nargs="*", help="Specific prompt IDs (e.g. 1.1 2.1)")
    parser.add_argument("--section", type=int, help="Run one section only")
    parser.add_argument("--output", type=str, help="Custom output directory")
    parser.add_argument(
        "--workers", type=int, default=5,
        help="Parallel workers (default 5; use 1 for sequential)",
    )
    parser.add_argument(
        "--gap", type=float, default=6.0,
        help="Min seconds between prompt starts in parallel mode (default 6)",
    )
    parser.add_argument(
        "--skip-existing", action="store_true",
        help="Skip prompts whose Q<id>_result.md already exists in the output dir",
    )
    args = parser.parse_args()

    prompts = parse_prompts_simple(_THIS_DIR / "test_prompts.md")
    if not prompts:
        print("No prompts found in test_prompts.md")
        return

    # Filter
    if args.ids:
        prompts = [(pid, p) for pid, p in prompts if pid in args.ids]
    elif args.section:
        prefix = f"{args.section}."
        prompts = [(pid, p) for pid, p in prompts if pid.startswith(prefix)]

    if not prompts:
        print("No matching prompts found.")
        return

    # Output directory
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = Path(args.output) if args.output else (_BENCHMARK_ROOT / f"test_run_{ts}")
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.skip_existing:
        done = {f.name[len("Q"):-len("_result.md")]
                for f in out_dir.glob("Q*_result.md")}
        skipped = sorted(pid for pid, _ in prompts if pid in done)
        if skipped:
            prompts = [(pid, p) for pid, p in prompts if pid not in done]
            print(f"Resume: skipping {len(skipped)} completed prompt(s): {skipped}")
        if not prompts:
            print("Resume: nothing left to run.")
            return

    mode = "sequential" if args.workers <= 1 else f"parallel ({args.workers} workers, {args.gap}s gap)"
    log.info("Running %d prompts [%s] -> %s", len(prompts), mode, out_dir)
    print(f"\nRunning {len(prompts)} prompts [{mode}] -> {out_dir}\n")

    # ── Per-run log file ────────────────────────────────────────
    _fh = setup_run_log(out_dir)

    # Callbacks
    def run_fn(pid, prompt_text):
        return run_one_prompt(pid, prompt_text, out_dir)

    def after_fn(_pid, result):
        write_result_md(out_dir / f"Q{result['prompt_id']}_result.md", result,
                        include_verdict=True)
        write_history_md(out_dir / f"Q{result['prompt_id']}_history.md", result,
                         rich_mode=True)
        ctx = result.get("final_context", "")
        if ctx:
            (out_dir / f"Q{result['prompt_id']}_final_context.md").write_text(
                ctx, encoding="utf-8")

    # Dispatch
    t_wall = time.time()
    if args.workers <= 1:
        results = run_sequential(prompts, run_fn, after_fn=after_fn,
                                 cooldown=10.0, log=log)
    else:
        results = run_parallel(prompts, run_fn, args.workers, args.gap,
                               after_fn=after_fn, log=log)
    wall_time = time.time() - t_wall

    # Summary + JSON trace
    write_summary_md(out_dir, results, wall_time, args.workers,
                     agent_name="Analysis Agent")
    write_json_trace(out_dir, results)

    n_ok = sum(1 for r in results if get_status(r) == "OK")
    n_err = sum(1 for r in results if get_status(r) == "ERROR")
    n_timeout = sum(1 for r in results if get_status(r) == "TIMEOUT")
    serial_time = sum(r["elapsed_s"] for r in results)
    total_tools = sum(len(r["tool_history"]) for r in results)

    log.info("=" * 60)
    log.info("DONE: %d OK,  %d errors,  %d timeouts,  %d total tools",
             n_ok, n_err, n_timeout, total_tools)
    if args.workers > 1 and wall_time > 0:
        log.info(
            "Wall time: %.0fs  |  Sum of prompt times: %.0fs  |  Speedup: %.1fx",
            wall_time, serial_time, serial_time / wall_time,
        )
    else:
        log.info("Total time: %.0fs", serial_time)
    log.info("Output: %s", out_dir)
    log.info("=" * 60)

    print(f"\nDone: {n_ok}/{len(results)} OK, {n_err} errors, {n_timeout} timeouts")
    print(f"Wall time: {wall_time:.0f}s | Serial sum: {serial_time:.0f}s | Tools: {total_tools}")
    print(f"Results: {out_dir}")

    teardown_run_log(_fh)


if __name__ == "__main__":
    main()
