#!/usr/bin/env python
"""
Test-runner for the ThermoML Query Agent (sequential + parallel).
=================================================================
Thin wrapper around shared test-runner helpers.  Agent-specific logic
is limited to ``run_one_prompt()`` which calls the query L0 orchestrator.

Usage:
    python run_tests.py                          # all prompts, 5 workers
    python run_tests.py 1.1 2.1 3.3              # specific IDs
    python run_tests.py --section 3              # entire section
    python run_tests.py --workers 1              # sequential
    python run_tests.py --workers 8 --gap 4      # 8 threads, 4s gap
"""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import sys
import time
from dataclasses import asdict
from pathlib import Path

# ── Project root setup ──────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).absolute().parent            # _DEBUG_script
PROJECT_ROOT = _SCRIPT_DIR.parent                        # NIST_ThermoML_query_agent
AGENT_ROOT = PROJECT_ROOT.parent                         # NIST_ThermoML_agents
WORKSPACE_ROOT = AGENT_ROOT.parent                       # ThermoML_research_agent

sys.path.insert(0, str(WORKSPACE_ROOT))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-5s | %(name)-18s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("TEST-RUNNER")

_BENCHMARK_ROOT = WORKSPACE_ROOT.parent / "_benchmark" / "Query"

# ── Shared helpers ──────────────────────────────────────────────────────────
from NIST_ThermoML_agents.general_db_query_engine.general_DEBUG_test_runner_helpers import (
    parse_prompts_with_sections,
    run_sequential,
    run_parallel,
    setup_run_log,
    teardown_run_log,
)
from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_tracking_hooks_output_helpers import (
    clean_answer,
    get_status,
    write_result_md,
    write_history_md,
    write_summary_md,
    write_json_trace,
)
from NIST_ThermoML_agents.NIST_ThermoML_query_agent.ThermoML_query_api import ThermoML_query_run as l0_run
from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import memory_management_MCP_tools as mem_tools
from NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_context_hooks.hook_catalog import (
    query_history_recorder as _query_history_recorder,
    save_final_context as _save_final_context,
)
from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_context_hooks import (
    history_tracking_hooks as _hr_mod,
)


# ═══════════════════════════════════════════════════════════════════════════
#  Run one prompt
# ═══════════════════════════════════════════════════════════════════════════

def run_one_prompt(
    prompt_id: str,
    prompt_text: str,
    output_dir: Path,
) -> dict:
    """Run a single prompt through the L0 orchestrator and return a
    standardised result dict (prompt_id, prompt_text, answer, …)."""

    # Each prompt gets its own subdirectory
    prompt_dir = output_dir / f"Q{prompt_id}"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    mem_path = prompt_dir / "working_memory.md"

    # Start real-time history recording
    try:
        history_path = prompt_dir / "run_history.md"
        _query_history_recorder.start_run(
            agent="query-agent",
            prompt=prompt_text,
            out_path=str(history_path),
        )
        # Patch base module singleton so react_loop inline imports use ours
        _hr_mod.history_recorder = _query_history_recorder
    except Exception as exc:
        log.warning("History recorder setup failed: %s", exc)

    log.info("=" * 60)
    log.info("PROMPT %s: %s", prompt_id, prompt_text[:80])
    log.info("=" * 60)

    t0 = time.time()
    try:
        result = l0_run(prompt_text, memory_path=mem_path)
        elapsed = time.time() - t0

        # Detect upstream errors relayed in the answer text
        answer = result.answer
        api_error = None
        if answer and answer.lstrip().startswith("Error:") and ("429" in answer[:300] or "RESOURCE_EXHAUSTED" in answer[:500]):
            api_error = "Upstream API rate-limit (429)"

        # Read final working memory snapshot
        try:
            working_memory = mem_tools.memory_read()
        except Exception:
            working_memory = ""

        output = {
            "prompt_id": prompt_id,
            "prompt_text": prompt_text,
            "answer": answer,
            "iterations": result.iterations,
            "elapsed_s": round(elapsed, 1),
            "timed_out": result.timed_out,
            "tool_history": result.tool_history,
            "error": api_error,
            "working_memory": working_memory,
            "final_context": getattr(result, "final_context", ""),
        }
    except Exception as e:
        elapsed = time.time() - t0
        log.error("PROMPT %s FAILED: %s", prompt_id, e, exc_info=True)
        output = {
            "prompt_id": prompt_id,
            "prompt_text": prompt_text,
            "answer": f"ERROR: {e}",
            "iterations": 0,
            "elapsed_s": round(elapsed, 1),
            "timed_out": False,
            "tool_history": [],
            "error": str(e),
            "working_memory": "",
            "final_context": "",
        }

    # Final flush of real-time history (ensures complete file)
    try:
        wm = output.get("working_memory", "")
        if wm:
            _query_history_recorder.set_working_memory(wm)
        status = "ERROR" if output.get("error") else ("TIMEOUT" if output.get("timed_out") else "OK")
        _query_history_recorder.set_final_status(status)
        _query_history_recorder.flush()
        _query_history_recorder.reset()
    except Exception as exc:
        log.warning("History recorder flush failed: %s", exc)
    try:
        _save_final_context(prompt_dir, output.get("final_context", ""))
    except Exception as exc:
        log.warning("Final context save failed: %s", exc)

    return output


# ═══════════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="ThermoML Agent Test Runner")
    parser.add_argument("ids", nargs="*", help="Specific prompt IDs to run (e.g. 1.1 2.1)")
    parser.add_argument("--section", type=str, help="Run all prompts in a section (e.g. 3)")
    parser.add_argument("--output", type=str, default=None, help="Output directory")
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
        help="Skip prompts whose Q<id>/result.md already exists in the output dir",
    )
    args = parser.parse_args()

    # Parse prompts
    prompts_path = _SCRIPT_DIR / "test_prompts.md"
    all_prompts = parse_prompts_with_sections(prompts_path)
    log.info("Parsed %d test prompts from %s", len(all_prompts), prompts_path)

    # Filter
    if args.ids:
        prompts = [p for p in all_prompts if p["id"] in args.ids]
    elif args.section:
        prompts = [p for p in all_prompts if p["section"] == args.section]
    else:
        prompts = all_prompts

    if not prompts:
        log.error("No prompts matched the filter. Available IDs: %s",
                  [p["id"] for p in all_prompts])
        sys.exit(1)

    # Output directory
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output) if args.output else (_BENCHMARK_ROOT / f"test_run_{ts}")
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.skip_existing:
        done = {d.name[len("Q"):] for d in output_dir.glob("Q*")
                if d.is_dir() and (d / "result.md").exists()}
        skipped = sorted(p["id"] for p in prompts if p["id"] in done)
        if skipped:
            prompts = [p for p in prompts if p["id"] not in done]
            print(f"Resume: skipping {len(skipped)} completed prompt(s): {skipped}")
        if not prompts:
            print("Resume: nothing left to run.")
            return

    mode = "sequential" if args.workers <= 1 else f"parallel ({args.workers} workers, {args.gap}s gap)"
    log.info("Running %d prompts [%s]: %s", len(prompts), mode, [p["id"] for p in prompts])

    # ── Per-run log file ────────────────────────────────────────
    _fh = setup_run_log(output_dir)

    # Convert to (pid, prompt_text) tuples for shared orchestration
    prompts_tuples = [(p["id"], p["prompt"]) for p in prompts]

    # Callbacks
    def run_fn(pid, prompt_text):
        return run_one_prompt(pid, prompt_text, output_dir)

    def after_fn(_pid, result):
        prompt_dir = output_dir / f"Q{result['prompt_id']}"
        prompt_dir.mkdir(parents=True, exist_ok=True)
        write_result_md(prompt_dir / "result.md", result, clean_fn=clean_answer)
        write_history_md(prompt_dir / "tool_trace.md", result, include_working_memory=True)

    # Dispatch
    wall_t0 = time.time()
    if args.workers <= 1:
        results = run_sequential(prompts_tuples, run_fn, after_fn=after_fn, log=log)
    else:
        results = run_parallel(prompts_tuples, run_fn, args.workers, args.gap,
                               after_fn=after_fn, log=log)
    wall_elapsed = time.time() - wall_t0

    # Summary + JSON trace
    write_summary_md(output_dir, results, wall_elapsed, args.workers,
                     agent_name="ThermoML Query Agent",
                     include_file_links=True, link_subdir=True)
    write_json_trace(output_dir, results)

    ok = sum(1 for r in results if get_status(r) == "OK")
    errs = sum(1 for r in results if get_status(r) == "ERROR")
    tos = sum(1 for r in results if get_status(r) == "TIMEOUT")
    serial_time = sum(r["elapsed_s"] for r in results)
    log.info("=" * 60)
    log.info("DONE: %d OK,  %d errors,  %d timeouts", ok, errs, tos)
    if args.workers > 1 and wall_elapsed > 0:
        log.info(
            "Wall time: %.0fs  |  Sum of prompt times: %.0fs  |  Speedup: %.1fx",
            wall_elapsed, serial_time, serial_time / wall_elapsed,
        )
    else:
        log.info("Total time: %.0fs", serial_time)
    log.info("Output: %s", output_dir)
    log.info("=" * 60)

    teardown_run_log(_fh)
if __name__ == "__main__":
    main()
