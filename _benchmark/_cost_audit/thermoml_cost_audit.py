"""ThermoML Anthropic-benchmark cost audit -- the single cost module of this folder.

Steps (command line, default = audit layers cache):
  audit  : exact per-call costs of the captured Main / Analysis / Query sessions (top-level
           + nested sub-agent captures), per-call tier labels joined from the Argo
           transcripts, log-estimated costs of the four uncaptured August Main prompts,
           per-prompt / per-tier CSVs and the PNG figures.
  layers : layer-aggregated horizontal figure (cost_layers_horizontal.png) and the
           OriginPro-ready TSV tables in originpro/ (reads the audit CSVs).
  cache  : state-control what-if -- every captured request replayed through a prefix
           cache model (5-min / 1-h / system-only / no-TTL on the current rendering, plus
           true per-thread state control), per prompt / call kind / thread.
  origin : editable OriginPro project of the per-family cost bars (six panels).
           Needs OriginPro (win32com) and the `layers` TSVs.

Scope: the benchmark tree in the parent folder (_benchmark); all
outputs are written next to this file.  Paths derive from __file__ (never .resolve() on N:).
"""
from __future__ import annotations

import csv
import json
import re
import statistics
import statistics as stats
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT = Path(__file__).absolute().parent          # .../_benchmark/_cost_audit
BENCH = OUT.parent                              # .../_benchmark
OUT.mkdir(exist_ok=True)
ODIR = OUT / "originpro"
ODIR.mkdir(exist_ok=True)


# ════ audit ═══════════════════════════════════════════════════════════════════════

TEST_PROMPTS_MD = (
    BENCH.parent / "ThermoML_research_agent" / "NIST_ThermoML_agents"
    / "_NIST_ThermoML_main_agent" / "_DEBUG_script" / "test_prompts.md"
)

# Assumed list prices, $/MTok (input, output) by Anthropic model prefix.
PRICES = {
    "claude-opus":   (5.00, 25.00),
    "claude-sonnet": (3.00, 15.00),
    "claude-haiku":  (1.00, 5.00),
}
ARGO_TO_ANTHROPIC_PREFIX = {
    "claudeopus": "claude-opus", "claudesonnet": "claude-sonnet",
    "claudehaiku": "claude-haiku",
}


def price_for(model: str) -> tuple[float, float]:
    m = (model or "").lower()
    for prefix, p in PRICES.items():
        if m.startswith(prefix):
            return p
    for argo, prefix in ARGO_TO_ANTHROPIC_PREFIX.items():
        if m.startswith(argo):
            return PRICES[prefix]
    return PRICES["claude-opus"]  # conservative default


def cost_usd(tin: int, tout: int, model: str) -> float:
    ri, ro = price_for(model)
    return tin / 1e6 * ri + tout / 1e6 * ro


def norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (t or "").lower())[:80]


# ── prompt-id tables ─────────────────────────────────────────────────────

def main_prompt_table() -> dict[str, str]:
    """norm(prompt) -> main test id, parsed from test_prompts.md tables."""
    out = {}
    for line in TEST_PROMPTS_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+(?:\.\d+)*)\s*\|\s*(.+?)\s*\|\s*$", line)
        if m:
            out[norm(m.group(2))] = m.group(1)
    return out


def analysis_prompt_table() -> dict[str, str]:
    """norm(prompt) -> Q id, from the Q*_result.md files."""
    d = BENCH / "Analysis" / "test_run_20260905_021947"
    out = {}
    for f in d.glob("Q*_result.md"):
        m = re.search(r"^\*\*Prompt:\*\*\s*(.+)$",
                      f.read_text(encoding="utf-8", errors="replace")[:4000], re.M)
        if m:
            out[norm(m.group(1))] = f.stem.removesuffix("_result")[1:]
    return out


def session_prompt(sdir: Path) -> str:
    h = sdir / "run_history.md"
    if not h.exists():
        return ""
    m = re.search(r"^\*\*Prompt:\*\*\s*(.+)$",
                  h.read_text(encoding="utf-8", errors="replace")[:6000], re.M)
    return m.group(1) if m else ""


# ── per-call tier labels from the session's Argo transcript ─────────────

EVENT_ROW = re.compile(
    r"\|\s*E\d+\s*\|[^|]*\|[^|]*\|\s*argo\s*\|[^|]*\|\s*"
    r"([\d,]+)\u00b7([\d,]+)\u2192([\d,]+)\s*\|[^|]*\|\s*`?([^|`]*)`?\s*\|\s*"
    r"([^|\u00b7]+)\u00b7\s*([^|\u00b7]+)\u00b7[^|]*\|")


def load_tier_queues(sdir: Path) -> dict[tuple[int, int], list[tuple[int, str, str]]]:
    """(system_chars, prompt_chars) -> FIFO of (response_chars, tier, event_tag)
    from run_history_detailed.md, for joining capture records to worker tiers."""
    md = sdir / "run_history_detailed.md"
    queues: dict[tuple[int, int], list[tuple[int, str, str]]] = {}
    if not md.exists():
        return queues
    for line in md.read_text(encoding="utf-8", errors="replace").splitlines():
        m = EVENT_ROW.match(line.strip())
        if not m:
            continue
        s, p, r = (int(x.replace(",", "")) for x in m.groups()[:3])
        queues.setdefault((s, p), []).append((r, m.group(6).strip(), m.group(4).strip()))
    return queues


def assign_tier(queues, rec) -> tuple[str, str]:
    """Greedy join: exact (sys,prompt,resp) pops its event; a same-(sys,prompt)
    retry/error attempt inherits the labels without consuming the event."""
    q = queues.get((rec["system_chars"], rec["prompt_chars"]))
    if not q:
        return "?", ""
    for i, (r, tier, tag) in enumerate(q):
        if r == rec["response_chars"]:
            q.pop(i)
            return tier, tag
    return q[0][1], q[0][2]


# ── captured-call parsing ────────────────────────────────────────────────

def parse_capture(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        u = (rec.get("response") or {}).get("usage") or {}
        tin, tout = u.get("input_tokens") or 0, u.get("output_tokens") or 0
        model = rec.get("anthropic_model") or rec.get("argo_model") or ""
        rows.append({
            "seq": rec.get("seq"), "ts": rec.get("ts"),
            "elapsed_s": rec.get("elapsed_s"),
            "argo_model": rec.get("argo_model"),
            "anthropic_model": rec.get("anthropic_model"),
            "status": rec.get("status_code"),
            "system_chars": rec.get("system_chars") or 0,
            "prompt_chars": rec.get("prompt_chars") or 0,
            "response_chars": rec.get("response_chars") or 0,
            "input_tokens": tin, "output_tokens": tout,
            "cache_creation_tokens": u.get("cache_creation_input_tokens") or 0,
            "cache_read_tokens": u.get("cache_read_input_tokens") or 0,
            "cost_usd": cost_usd(tin, tout, model),
        })
    return rows


def sub_role(rel: Path) -> str:
    parts = rel.parts
    if "query_runs" in parts:
        return "query_sub"
    if "analysis_runs" in parts:
        return "analysis_sub"
    return "top"


# ── session discovery ────────────────────────────────────────────────────

def collect_sessions():
    """[(phase, prompt_id, session_dir, session_tag)] for captured runs."""
    mtab, atab = main_prompt_table(), analysis_prompt_table()
    sessions = []
    for sdir in sorted((BENCH / "Main").glob("run_20260905_*")):
        pid = mtab.get(norm(session_prompt(sdir)))
        sessions.append(("Main", pid or f"?{sdir.name[-8:]}", sdir))
    for sdir in sorted((BENCH / "Analysis").glob("run_20260905_*")):
        pid = atab.get(norm(session_prompt(sdir)))
        sessions.append(("Analysis", pid or f"?{sdir.name[-8:]}", sdir))
    for sdir in sorted((BENCH / "Query" / "test_run_20260905_021947").glob("Q*")):
        if sdir.is_dir():
            sessions.append(("Query", sdir.name[1:], sdir))
    return sessions


# ── August (uncaptured) estimation from reference_stats tier tables ─────

TIER_ROW = re.compile(
    r"^\|\s*([^|*]+?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|"
    r"\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*[\d,]+\s*\|\s*[\d.]+\s*\|\s*([^|]*)\|")


def parse_tier_table(md: Path) -> list[dict]:
    rows = []
    text = md.read_text(encoding="utf-8", errors="replace")
    sec = text.split("## 1. Argo API Call Summary", 1)[-1].split("\n## ", 1)[0]
    for line in sec.splitlines():
        m = TIER_ROW.match(line.strip())
        if not m or m.group(1).strip().upper() == "TIER":
            continue
        tier, calls, sysc, prc, rsc, sent = (m.group(1).strip(),
                                             *(int(x.replace(",", "")) for x in m.groups()[1:6]))
        model = (m.group(7) or "").strip().split(",")[0].strip()
        rows.append({"tier": tier, "calls": calls, "system_chars": sysc,
                     "prompt_chars": prc, "response_chars": rsc,
                     "sent_chars": sent, "model": model})
    return rows


def august_sessions():
    mtab = main_prompt_table()
    out = []
    for sdir in sorted((BENCH / "Main").glob("run_20260815_*")):
        pid = mtab.get(norm(session_prompt(sdir)))
        out.append((pid or f"?{sdir.name[-8:]}", sdir))
    return out


# ── run it ───────────────────────────────────────────────────────────────

def run_audit() -> None:
    sessions = collect_sessions()

    # 1. parse all captures, keyed per session
    call_rows, per_session = [], {}
    for phase, pid, sdir in sessions:
        tag = "_".join(sdir.name.split("_")[1:3]) if sdir.name.startswith("run_") else sdir.name
        agg = {}
        for cap in sorted(sdir.rglob("anthropic_raw_capture.jsonl")):
            role = sub_role(cap.parent.relative_to(sdir))
            queues = load_tier_queues(cap.parent)
            for r in parse_capture(cap):
                ev_tier, ev_tag = assign_tier(queues, r)
                r.update(phase=phase, prompt_id=pid, session=sdir.name, role=role,
                         tier=ev_tier, event_tag=ev_tag)
                call_rows.append(r)
                a = agg.setdefault(role, [0, 0, 0, 0.0])
                a[0] += 1; a[1] += r["input_tokens"]; a[2] += r["output_tokens"]
                a[3] += r["cost_usd"]
        per_session[(phase, pid, sdir.name)] = (tag, agg)

    # 2. canonical vs superseded (latest session per prompt wins)
    latest = {}
    for (phase, pid, sname), (tag, _) in per_session.items():
        k = (phase, pid)
        if k not in latest or tag > latest[k][0]:
            latest[k] = (tag, sname)
    superseded = {(p, i, s): latest[(p, i)][1] != s for (p, i, s) in per_session}

    # 3. calibration ratios from OK captured calls
    cin = ctin = cout = ctout = 0
    for r in call_rows:
        if r["status"] == 200 and r["input_tokens"]:
            cin += r["system_chars"] + r["prompt_chars"]; ctin += r["input_tokens"]
            cout += r["response_chars"]; ctout += r["output_tokens"]
    r_in, r_out = cin / ctin, cout / ctout
    print(f"calibration: {r_in:.3f} input chars/token, {r_out:.3f} output chars/token "
          f"(from {ctin:,} in-tok / {ctout:,} out-tok)")

    # 4. August estimation
    est_rows, est_session = [], {}
    for pid, sdir in august_sessions():
        agg = {}
        for md in sorted(sdir.rglob("reference_stats.md")):
            role = sub_role(md.parent.relative_to(sdir))
            for t in parse_tier_table(md):
                tin = round((t["system_chars"] + t["prompt_chars"]) / r_in)
                tout = round(t["response_chars"] / r_out)
                c = cost_usd(tin, tout, t["model"])
                est_rows.append({
                    "phase": "Main", "prompt_id": pid, "session": sdir.name,
                    "role": role, "tier": t["tier"], "calls": t["calls"],
                    "model": t["model"],
                    "input_chars": t["system_chars"] + t["prompt_chars"],
                    "response_chars": t["response_chars"],
                    "est_input_tokens": tin, "est_output_tokens": tout,
                    "est_cost_usd": c,
                })
                a = agg.setdefault(role, [0, 0, 0, 0.0])
                a[0] += t["calls"]; a[1] += tin; a[2] += tout; a[3] += c
        est_session[(pid, sdir.name)] = agg

    # 5. CSV exports
    with open(OUT / "anthropic_calls_full.csv", "w", newline="", encoding="utf-8") as fh:
        cols = ["phase", "prompt_id", "session", "role", "tier", "event_tag",
                "seq", "ts", "elapsed_s", "argo_model", "anthropic_model",
                "status", "system_chars",
                "prompt_chars", "response_chars", "input_tokens", "output_tokens",
                "cache_creation_tokens", "cache_read_tokens", "cost_usd"]
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader(); w.writerows(call_rows)

    # per worker-tier rollup (captured exact + August estimated)
    tier_agg: dict[tuple, list] = {}
    for r in call_rows:
        k = (r["phase"], r["prompt_id"], r["session"], r["role"], r["tier"], False)
        a = tier_agg.setdefault(k, [0, 0, 0, 0.0])
        a[0] += 1; a[1] += r["input_tokens"]; a[2] += r["output_tokens"]
        a[3] += r["cost_usd"]
    for e in est_rows:
        k = ("Main", e["prompt_id"], e["session"], e["role"], e["tier"], True)
        a = tier_agg.setdefault(k, [0, 0, 0, 0.0])
        a[0] += e["calls"]; a[1] += e["est_input_tokens"]
        a[2] += e["est_output_tokens"]; a[3] += e["est_cost_usd"]
    tier_rows = [{"phase": p, "prompt_id": i, "session": s, "role": ro,
                  "tier": t, "estimated": est, "calls": a[0],
                  "input_tokens": a[1], "output_tokens": a[2],
                  "cost_usd": round(a[3], 4)}
                 for (p, i, s, ro, t, est), a in sorted(tier_agg.items())]
    with open(OUT / "per_tier_costs.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(tier_rows[0]))
        w.writeheader(); w.writerows(tier_rows)

    with open(OUT / "estimated_calls_august.csv", "w", newline="", encoding="utf-8") as fh:
        cols = ["phase", "prompt_id", "session", "role", "tier", "calls", "model",
                "input_chars", "response_chars", "est_input_tokens",
                "est_output_tokens", "est_cost_usd"]
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader(); w.writerows(est_rows)

    prompt_rows = []
    for (phase, pid, sname), (tag, agg) in sorted(per_session.items()):
        tot = [sum(a[i] for a in agg.values()) for i in range(4)]
        prompt_rows.append({
            "phase": phase, "prompt_id": pid, "session": sname,
            "estimated": False, "superseded": superseded[(phase, pid, sname)],
            "calls": tot[0], "input_tokens": tot[1], "output_tokens": tot[2],
            "cost_total_usd": round(tot[3], 4),
            "cost_top_usd": round(agg.get("top", [0]*4)[3], 4),
            "cost_query_subs_usd": round(agg.get("query_sub", [0]*4)[3], 4),
            "cost_analysis_subs_usd": round(agg.get("analysis_sub", [0]*4)[3], 4),
        })
    for (pid, sname), agg in sorted(est_session.items()):
        tot = [sum(a[i] for a in agg.values()) for i in range(4)]
        prompt_rows.append({
            "phase": "Main", "prompt_id": pid, "session": sname,
            "estimated": True, "superseded": False,
            "calls": tot[0], "input_tokens": tot[1], "output_tokens": tot[2],
            "cost_total_usd": round(tot[3], 4),
            "cost_top_usd": round(agg.get("top", [0]*4)[3], 4),
            "cost_query_subs_usd": round(agg.get("query_sub", [0]*4)[3], 4),
            "cost_analysis_subs_usd": round(agg.get("analysis_sub", [0]*4)[3], 4),
        })
    with open(OUT / "per_prompt_costs.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(prompt_rows[0]))
        w.writeheader(); w.writerows(prompt_rows)

    # 6. per-phase stats (canonical, non-superseded; August estimates included in Main)
    canon = [r for r in prompt_rows if not r["superseded"]]
    stat_rows = []
    for phase in ("Main", "Analysis", "Query"):
        costs = [r["cost_total_usd"] for r in canon if r["phase"] == phase]
        subs = [r["cost_query_subs_usd"] + r["cost_analysis_subs_usd"]
                for r in canon if r["phase"] == phase]
        stat_rows.append({
            "phase": phase, "prompts": len(costs), "total_usd": round(sum(costs), 2),
            "mean_usd": round(stats.mean(costs), 3),
            "median_usd": round(stats.median(costs), 3),
            "min_usd": round(min(costs), 3), "max_usd": round(max(costs), 3),
            "stdev_usd": round(stats.stdev(costs), 3) if len(costs) > 1 else 0.0,
            "subagent_share": round(sum(subs) / sum(costs), 3) if sum(costs) else 0.0,
        })
    with open(OUT / "phase_stats.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(stat_rows[0]))
        w.writeheader(); w.writerows(stat_rows)

    # 7. plots
    def pkey(pid):
        try:
            return [int(x) for x in pid.split(".")]
        except ValueError:
            return [99]

    fig, axes = plt.subplots(3, 1, figsize=(13, 12))
    colors = {"top": "#4c72b0", "query_sub": "#dd8452", "analysis_sub": "#55a868"}
    for ax, phase in zip(axes, ("Main", "Analysis", "Query")):
        rows = sorted((r for r in canon if r["phase"] == phase),
                      key=lambda r: pkey(r["prompt_id"]))
        xs = range(len(rows))
        bot = [0.0] * len(rows)
        for part, lbl in (("cost_top_usd", "agent itself"),
                          ("cost_query_subs_usd", "query subagents"),
                          ("cost_analysis_subs_usd", "analysis subagents")):
            vals = [r[part] for r in rows]
            key = part.split("_", 1)[1].rsplit("_", 1)[0]
            ax.bar(xs, vals, bottom=bot,
                   color=colors["top" if "top" in part else
                                "query_sub" if "query" in part else "analysis_sub"],
                   label=lbl,
                   hatch=None, edgecolor="white", linewidth=0.4)
            bot = [b + v for b, v in zip(bot, vals)]
        for i, r in enumerate(rows):  # hatch overlay for estimated prompts
            if r["estimated"]:
                ax.bar([i], [r["cost_total_usd"]], fill=False, hatch="///",
                       edgecolor="black", linewidth=0.6)
        ax.set_xticks(list(xs))
        ax.set_xticklabels([r["prompt_id"] + ("*" if r["estimated"] else "")
                            for r in rows], rotation=45, ha="right", fontsize=8)
        ax.set_ylabel("cost (USD)")
        tot = sum(r["cost_total_usd"] for r in rows)
        ax.set_title(f"{phase} agent — per-prompt Anthropic cost "
                     f"({len(rows)} prompts, total ${tot:.2f})", fontsize=11)
        ax.grid(axis="y", alpha=0.3)
    axes[0].legend(fontsize=9)
    axes[0].text(0.995, 0.95, "* = estimated from Argo char transcript\n"
                 "(no Anthropic capture; Aug-15 runs)",
                 transform=axes[0].transAxes, ha="right", va="top", fontsize=8,
                 bbox=dict(fc="lightyellow", ec="gray"))
    fig.suptitle("ThermoML benchmark — Anthropic API cost per prompt "
                 "(opus $5/$25, sonnet $3/$15 per MTok assumed)", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(OUT / "cost_per_prompt.png", dpi=200)

    fig2, ax2 = plt.subplots(figsize=(7, 5))
    data = [[r["cost_total_usd"] for r in canon if r["phase"] == p]
            for p in ("Main", "Analysis", "Query")]
    ax2.boxplot(data, tick_labels=["Main", "Analysis", "Query"], showmeans=True)
    for i, d in enumerate(data, 1):
        ax2.scatter([i + 0.08] * len(d), d, s=14, alpha=0.6, color="#4c72b0")
    ax2.set_ylabel("per-prompt cost (USD)")
    ax2.set_title("Per-prompt cost distribution by agent phase")
    ax2.grid(axis="y", alpha=0.3)
    fig2.tight_layout()
    fig2.savefig(OUT / "cost_distributions.png", dpi=200)

    # worker-layer decomposition per phase (canonical sessions only)
    canon_keys = {(r["phase"], r["prompt_id"], r["session"]) for r in canon}
    phase_tier: dict[str, dict[str, float]] = {}
    for t in tier_rows:
        if (t["phase"], t["prompt_id"], t["session"]) not in canon_keys:
            continue
        label = t["tier"] if t["role"] == "top" else f"{t['role'].split('_')[0]}-sub {t['tier']}"
        phase_tier.setdefault(t["phase"], {}).setdefault(label, 0.0)
        phase_tier[t["phase"]][label] += t["cost_usd"]
    fig3, ax3 = plt.subplots(figsize=(11, 6))
    phases = ("Main", "Analysis", "Query")
    labels = sorted({l for d in phase_tier.values() for l in d},
                    key=lambda l: (-max(d.get(l, 0) for d in phase_tier.values())))
    cmap = plt.get_cmap("tab20")
    bot = [0.0] * len(phases)
    for j, lbl in enumerate(labels):
        vals = [phase_tier.get(p, {}).get(lbl, 0.0) for p in phases]
        ax3.bar(phases, vals, bottom=bot, label=lbl, color=cmap(j % 20),
                edgecolor="white", linewidth=0.4)
        for i, (b, v) in enumerate(zip(bot, vals)):
            if v > 3.5:
                ax3.text(i, b + v / 2, f"{lbl}\n${v:.0f}", ha="center",
                         va="center", fontsize=7)
        bot = [b + v for b, v in zip(bot, vals)]
    ax3.set_ylabel("phase total cost (USD)")
    ax3.set_title("Worker-layer cost decomposition per phase (canonical runs; "
                  "Main includes nested subagent sessions + estimated Aug prompts)")
    ax3.legend(fontsize=7, ncols=2, loc="upper right")
    ax3.grid(axis="y", alpha=0.3)
    fig3.tight_layout()
    fig3.savefig(OUT / "cost_worker_layers.png", dpi=200)

    # 8. console summary
    print(f"\ncaptured calls: {len(call_rows):,}   sessions: {len(per_session)}"
          f"   estimated Aug sessions: {len(est_session)}")
    for s in stat_rows:
        print(f"  {s['phase']:<9} n={s['prompts']:>2}  total=${s['total_usd']:>7.2f}  "
              f"mean=${s['mean_usd']:>6.3f}  median=${s['median_usd']:>6.3f}  "
              f"range=${s['min_usd']:.2f}–${s['max_usd']:.2f}  "
              f"subagent share={s['subagent_share']:.0%}")
    sup = [(p, i, s) for (p, i, s), v in superseded.items() if v]
    if sup:
        print("superseded sessions (excluded from stats, kept in CSVs):")
        for p, i, s in sup:
            print(f"  {p} {i}: {s}")
    unk = sorted({(r["phase"], r["prompt_id"]) for r in prompt_rows
                  if str(r["prompt_id"]).startswith("?")})
    if unk:
        print("UNMAPPED sessions:", unk)
    n_unjoined = sum(1 for r in call_rows if r["tier"] == "?")
    print(f"tier join: {len(call_rows) - n_unjoined}/{len(call_rows)} capture "
          f"records matched to transcript tiers")
    print("\nworker-layer cost by phase (canonical):")
    for p in phases:
        for lbl, v in sorted(phase_tier.get(p, {}).items(), key=lambda kv: -kv[1]):
            print(f"  {p:<9} {lbl:<28} ${v:8.2f}")
    print(f"\noutputs -> {OUT}")


# ════ layers (figure + Origin-ready tables) ═══════════════════════════════════════

def run_layers() -> None:
    """Horizontal layer figure + OriginPro-ready TSV tables (reads per_prompt_costs.csv / per_tier_costs.csv)."""
    MAIN_FAMS = ["1.1", "1.2", "2", "3", "4"]
    Q_FAMS = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]


    def family(phase: str, pid: str) -> str:
        if phase == "Main":
            return pid if pid.startswith(("1.1", "1.2")) and pid.count(".") >= 2 \
                else pid.split(".")[0]
        return "Q" + pid.split(".")[0]


    def fam_of(phase, pid):
        f = family(phase, pid)
        return ".".join(f.split(".")[:2]) if phase == "Main" and f.count(".") >= 2 else f


    # ── load canonical rows ──────────────────────────────────────────────────

    with open(OUT / "per_prompt_costs.csv", encoding="utf-8") as fh:
        pp = [r for r in csv.DictReader(fh) if r["superseded"] == "False"]
    canon_sessions = {(r["phase"], r["prompt_id"], r["session"]) for r in pp}

    with open(OUT / "per_tier_costs.csv", encoding="utf-8") as fh:
        pt = [r for r in csv.DictReader(fh)
              if (r["phase"], r["prompt_id"], r["session"]) in canon_sessions]

    # per-prompt totals + role components
    prompts: dict[tuple, dict] = {}
    for r in pp:
        k = (r["phase"], r["prompt_id"])
        prompts[k] = {
            "family": fam_of(r["phase"], r["prompt_id"]),
            "estimated": r["estimated"] == "True",
            "total": float(r["cost_total_usd"]),
            "top": float(r["cost_top_usd"]),
            "query_sub": float(r["cost_query_subs_usd"]),
            "analysis_sub": float(r["cost_analysis_subs_usd"]),
        }


    def tier_bucket(phase: str, role: str, tier: str) -> str:
        if phase != "Main":
            return tier if tier in ("L0-main", "L1-worker") else "other"
        pre = {"top": "own", "query_sub": "q-sub", "analysis_sub": "a-sub"}[role]
        if tier == "L0-main":
            return f"{pre} L0-main"
        if tier == "L1-worker":
            return f"{pre} L1-worker"
        return f"{pre} misc"


    tiers_per_prompt: dict[tuple, dict] = defaultdict(lambda: defaultdict(float))
    for r in pt:
        k = (r["phase"], r["prompt_id"])
        tiers_per_prompt[k][tier_bucket(r["phase"], r["role"], r["tier"])] += float(r["cost_usd"])

    SEGS_ROLE = {"Main": [("top", "agent itself"), ("query_sub", "query subagents"),
                          ("analysis_sub", "analysis subagents")],
                 "Analysis": [("top", "agent total")],
                 "Query": [("top", "agent total")]}
    SEGS_TIER = {
        "Main": ["own L0-main", "own L1-worker", "own misc",
                 "q-sub L0-main", "q-sub L1-worker", "q-sub misc",
                 "a-sub L0-main", "a-sub L1-worker", "a-sub misc"],
        "Analysis": ["L0-main", "L1-worker", "other"],
        "Query": ["L0-main", "L1-worker", "other"],
    }
    ROLE_COLORS = {"top": "#4c72b0", "query_sub": "#dd8452", "analysis_sub": "#55a868"}
    TIER_COLORS = {
        "own L0-main": "#2f4b7c", "own L1-worker": "#6e8fc9", "own misc": "#b9c9e8",
        "q-sub L0-main": "#b35a1f", "q-sub L1-worker": "#e8945a", "q-sub misc": "#f5c9a8",
        "a-sub L0-main": "#2e6b45", "a-sub L1-worker": "#6fb98f", "a-sub misc": "#bfe3cf",
        "L0-main": "#2f4b7c", "L1-worker": "#6e8fc9", "other": "#b9c9e8",
    }


    def fam_stats(vals):
        v = np.array(vals, float)
        return dict(n=len(v), mean=v.mean(), median=np.median(v),
                    p10=np.percentile(v, 10), p90=np.percentile(v, 90),
                    min=v.min(), max=v.max())


    # ── assemble per (agent, mode, family): segment means + totals ───────────

    table_rows, stats_rows, dot_rows = [], [], []
    panel_data = {}
    for phase, fams in (("Main", MAIN_FAMS), ("Analysis", Q_FAMS), ("Query", Q_FAMS)):
        for mode in ("sessions", "workers"):
            per_fam = {}
            for fam in fams:
                ks = [k for k, p in prompts.items() if k[0] == phase and p["family"] == fam]
                if not ks:
                    continue
                totals = [prompts[k]["total"] for k in ks]
                if mode == "sessions":
                    segs = {lbl: float(np.mean([prompts[k][key] for k in ks]))
                            for key, lbl in SEGS_ROLE[phase]}
                    colors = {lbl: ROLE_COLORS[key] for key, lbl in SEGS_ROLE[phase]}
                else:
                    segs = {b: float(np.mean([tiers_per_prompt[k].get(b, 0.0) for k in ks]))
                            for b in SEGS_TIER[phase]}
                    segs = {b: v for b, v in segs.items() if v > 1e-9}
                    colors = {b: TIER_COLORS[b] for b in segs}
                st = fam_stats(totals)
                per_fam[fam] = dict(segs=segs, colors=colors, stats=st,
                                    dots=[(prompts[k]["total"], prompts[k]["estimated"],
                                           k[1]) for k in ks])
                for lbl, v in segs.items():
                    table_rows.append({"agent": phase, "mode": mode, "family": fam,
                                       "segment": lbl, "mean_cost_usd": round(v, 4),
                                       "n_prompts": st["n"]})
                if mode == "sessions":
                    stats_rows.append({"agent": phase, "family": fam, **{
                        kk: (st[kk] if kk == "n" else round(st[kk], 4)) for kk in st}})
                    for tot, est, pid in per_fam[fam]["dots"]:
                        dot_rows.append({"agent": phase, "family": fam, "prompt_id": pid,
                                         "estimated": est, "total_cost_usd": round(tot, 4)})
            panel_data[(phase, mode)] = per_fam

    # ── OriginPro-ready TSVs ─────────────────────────────────────────────────

    def write_tsv(path: Path, rows: list[dict]):
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
            w.writeheader(); w.writerows(rows)


    write_tsv(ODIR / "layer_segment_means_Origin_ready.tsv", table_rows)
    write_tsv(ODIR / "layer_stats_Origin_ready.tsv", stats_rows)
    write_tsv(ODIR / "layer_prompt_totals_Origin_ready.tsv", dot_rows)

    # wide sheets (families as rows, segments as columns) for direct stacked-bar plots
    for (phase, mode), per_fam in panel_data.items():
        seg_names = list(dict.fromkeys(s for pf in per_fam.values() for s in pf["segs"]))
        rows = []
        for fam, pf in per_fam.items():
            st = pf["stats"]
            rows.append({"family": fam,
                         **{s: round(pf["segs"].get(s, 0.0), 4) for s in seg_names},
                         "mean_total": round(st["mean"], 4), "median": round(st["median"], 4),
                         "p10": round(st["p10"], 4), "p90": round(st["p90"], 4),
                         "min": round(st["min"], 4), "max": round(st["max"], 4),
                         "n": st["n"]})
        write_tsv(ODIR / f"layers_wide_{phase}_{mode}_Origin_ready.tsv", rows)

    # ── figure ───────────────────────────────────────────────────────────────

    fig, axes = plt.subplots(3, 2, figsize=(14, 13))
    MODES = (("sessions", "by subagent sessions"), ("workers", "by worker layers"))
    for row, phase in enumerate(("Main", "Analysis", "Query")):
        xmax = 0.0
        for col, (mode, mode_lbl) in enumerate(MODES):
            ax = axes[row][col]
            per_fam = panel_data[(phase, mode)]
            fams = [f for f in (MAIN_FAMS if phase == "Main" else Q_FAMS) if f in per_fam]
            ys = np.arange(len(fams))[::-1]  # first family on top
            seg_names = list(dict.fromkeys(s for f in fams for s in per_fam[f]["segs"]))
            left = np.zeros(len(fams))
            for s in seg_names:
                vals = np.array([per_fam[f]["segs"].get(s, 0.0) for f in fams])
                seg_color = next((per_fam[f]["colors"][s] for f in fams
                                  if s in per_fam[f]["colors"]), "#999999")
                ax.barh(ys, vals, left=left, height=0.52, color=seg_color,
                        label=s, edgecolor="white", linewidth=0.5)
                left += vals
            for y, f in zip(ys, fams):
                st = per_fam[f]["stats"]
                # stats symbols on the bar centerline
                ax.plot(st["median"], y, marker="|", ms=22, mew=2.4, color="black")
                ax.plot(st["mean"], y, marker="D", ms=7, color="black",
                        mfc="white", mew=1.6)
                ax.plot(st["p10"], y, marker=">", ms=6, color="black", mfc="none", mew=1.2)
                ax.plot(st["p90"], y, marker="<", ms=6, color="black", mfc="none", mew=1.2)
                for edge in (st["min"], st["max"]):
                    ax.plot(edge, y, marker="x", ms=6, color="#b22222", mew=1.6)
                # per-prompt total dots in a band above the bar
                dots = per_fam[f]["dots"]
                off = np.linspace(-0.07, 0.07, len(dots)) if len(dots) > 1 else [0.0]
                for (tot, est, _pid), dy in zip(sorted(dots), off):
                    ax.plot(tot, y + 0.38 + dy, marker="o", ms=4.5,
                            color="#333333", mfc="none" if est else "#333333",
                            mew=1.1, alpha=0.85, linestyle="none")
                xmax = max(xmax, st["max"])
            ax.set_yticks(ys)
            ax.set_yticklabels([f"{f}  (n={per_fam[f]['stats']['n']})" for f in fams],
                               fontsize=9)
            ax.set_title(f"{phase} — {mode_lbl}", fontsize=11)
            ax.grid(axis="x", alpha=0.3)
            ax.legend(fontsize=7, loc="lower right", ncols=1 if col == 0 else 2)
            if row == 2:
                ax.set_xlabel("cost per prompt (USD)")
        for col in (0, 1):
            axes[row][col].set_xlim(0, xmax * 1.08)

    sym = [Line2D([], [], marker="o", ls="none", color="#333", mfc="#333", ms=5,
                  label="prompt total"),
           Line2D([], [], marker="o", ls="none", color="#333", mfc="none", ms=5,
                  label="prompt total (estimated Aug)"),
           Line2D([], [], marker="D", ls="none", color="black", mfc="white", ms=7,
                  label="mean (= bar length)"),
           Line2D([], [], marker="|", ls="none", color="black", ms=12, mew=2.4,
                  label="median"),
           Line2D([], [], marker=">", ls="none", color="black", mfc="none", ms=6,
                  label="p10"),
           Line2D([], [], marker="<", ls="none", color="black", mfc="none", ms=6,
                  label="p90"),
           Line2D([], [], marker="x", ls="none", color="#b22222", ms=6,
                  label="min / max edge cases")]
    fig.legend(handles=sym, loc="lower center", ncols=7, fontsize=8, frameon=False)
    fig.suptitle("ThermoML benchmark — layer-aggregated Anthropic cost per prompt\n"
                 "stacked segments = family means of component costs "
                 "(opus $5/$25, sonnet $3/$15 per MTok assumed)", fontsize=12)
    fig.tight_layout(rect=(0, 0.035, 1, 0.955))
    fig.savefig(OUT / "cost_layers_horizontal.png", dpi=200)
    print("figure -> cost_layers_horizontal.png")
    print("origin tables ->", *(p.name for p in sorted(ODIR.glob("*.tsv"))), sep="\n  ")


# ════ cache (state-control what-if) ═══════════════════════════════════════════════

READ_MULT = 0.10
STATECTL = "statectl"   # thread-based true state control (append-only per agent thread, no TTL)
# minimum cacheable prompt length per model family (platform docs, 2026-09)
MIN_CACHEABLE = {"claude-opus-4-6": 4096, "claude-opus-4-5": 4096, "claude-opus-4-7": 2048,
                 "claude-sonnet-4-6": 1024, "claude-sonnet-4-5": 1024, "claude-haiku-4-5": 4096}
CACHE_VARIANTS = {
    "cache5m": (300.0, 1.25, "blocks"),
    "cache1h": (3600.0, 2.00, "blocks"),
    "sysonly5m": (300.0, 1.25, "system"),
    "ideal": (float("inf"), 1.25, "blocks"),
}
VN = list(CACHE_VARIANTS) + [STATECTL]

_TURN = re.compile(r"_\[Turn#\d+\]")
_FORK = re.compile(r"_\[(compaction-guidance|ReAct-hard-stop|gate-rewrite)\]$")


def thread_of(tag: str) -> tuple[str, bool]:
    """(thread key, is_fork).  ReAct turns of one agent instance share a thread; a
    compaction-guidance / hard-stop / gate-rewrite call forks from that thread's state."""
    t = _TURN.sub("", tag or "")
    if _FORK.search(t):
        return _FORK.sub("_[ReAct]", t), True
    return t, False


def kind_of(tag: str, role: str) -> str:
    g = re.sub(r"\[[0-9a-f]{8}\]_", "", _TURN.sub("", tag or ""))
    g = re.sub(r"#\d+", "#", g)
    if g.endswith("[compaction-guidance]"):
        return "compaction-guidance (full-transcript fork)"
    if g.endswith("[ReAct-hard-stop]") or g.endswith("[gate-rewrite]"):
        return "L1 worker hard-stop/gate-rewrite turn"
    if g.endswith("[ReAct]"):
        if "[L1#]" in g:
            return "L1 query-worker loop"
        if g.startswith("[Main]_[A#]") or g.startswith("[A]"):
            return "Analysis agent loop"
        if g.startswith("[Main]_[Q#]") or g.startswith("[Q]"):
            return "Query orchestrator loop"
        return "Main orchestrator loop"
    if "agent_run_verdict" in g:
        return "verdict (single-shot)"
    if "[L0-menu-planner]" in g:
        return "menu planner (single-shot)"
    if "[Tool#]" in g or "[L1-subagent]" in g:
        return "data-extraction subagent (single-shot)"
    return "post-answer hook constructors (single-shot)"


def min_cacheable(model: str) -> int:
    m = (model or "").lower()
    for prefix, v in MIN_CACHEABLE.items():
        if m.startswith(prefix):
            return v
    return 4096


def parse_capture_texts(path: Path, role: str) -> list[dict]:
    queues = load_tier_queues(path.parent)
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        u = (rec.get("response") or {}).get("usage") or {}
        tin, tout = u.get("input_tokens") or 0, u.get("output_tokens") or 0
        if not tin:
            continue
        model = rec.get("anthropic_model") or rec.get("argo_model") or ""
        req = rec.get("request") or {}
        system = req.get("system") or ""
        if isinstance(system, list):
            system = " ".join(b.get("text", "") for b in system if isinstance(b, dict))
        parts = [system]
        for m in req.get("messages") or []:
            c = m.get("content")
            if isinstance(c, list):
                c = "".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in c)
            parts.append(f"\x00{m.get('role')}\x00{c}")
        r = {
            "seq": rec.get("seq"), "ts": rec.get("ts"),
            "ts_epoch": datetime.fromisoformat(rec["ts"]).timestamp(),
            "elapsed_s": float(rec.get("elapsed_s") or 0),
            "model": model, "role": role,
            "system_chars": rec.get("system_chars") or 0,
            "prompt_chars": rec.get("prompt_chars") or 0,
            "response_chars": rec.get("response_chars") or 0,
            "input_tokens": tin, "output_tokens": tout,
            "_system": system, "_prompt": "\x01".join(parts),
        }
        r["tier"], r["event_tag"] = assign_tier(queues, r)
        r["thread"], r["is_fork"] = thread_of(r["event_tag"])
        if not r["event_tag"]:
            r["thread"] = f"{role}|{r['tier']}|sys{len(system)}"  # untagged call: stable key
        r["kind"] = kind_of(r["event_tag"], role)
        ri, ro = price_for(model)
        r["cost_in_usd"], r["cost_out_usd"] = tin / 1e6 * ri, tout / 1e6 * ro
        rows.append(r)
    return rows


def simulate_cache(rows: list[dict]) -> None:
    """Annotate rows with <v>_read/_write/_uncached_tokens, <v>_cost_usd, <v>_hit
    (hit kind: 'state' = previous turn is a verbatim prefix, 'system', or '')."""
    def start_of(r):
        return r["ts_epoch"] - r["elapsed_s"]
    order = sorted(range(len(rows)), key=lambda i: (start_of(rows[i]), rows[i]["seq"] or 0))
    for name, (ttl, wmult, mode) in CACHE_VARIANTS.items():
        full: list[dict] = []
        sysc: dict[str, dict] = {}
        for i in order:
            r = rows[i]
            P, S, T = r["_prompt"], r["_system"], r["input_tokens"]
            mn = min_cacheable(r["model"])
            now = start_of(r)
            n = max(len(P), 1)
            full = [e for e in full if now - e["last"] <= ttl]
            hit_chars, hit_entry, kind = 0, None, ""
            if mode == "blocks":
                for e in full:
                    if e["avail"] <= now and len(e["prompt"]) > hit_chars and P.startswith(e["prompt"]):
                        hit_chars, hit_entry = len(e["prompt"]), e
                if hit_entry is not None:
                    kind = "state"
            se = sysc.get(S)
            sys_live = bool(S) and se is not None and now - se["last"] <= ttl and se["avail"] <= now
            if hit_chars == 0 and sys_live:
                hit_chars, kind = len(S), "system"
            read = round(T * hit_chars / n)
            if read < mn:
                read, hit_entry, kind = 0, None, ""
            rest = T - read
            write, unc = (rest, 0) if T >= mn else (0, rest)
            ri, ro = price_for(r["model"])
            r[f"{name}_read_tokens"], r[f"{name}_write_tokens"], r[f"{name}_uncached_tokens"] = read, write, unc
            r[f"{name}_hit"] = kind
            r[f"{name}_cost_usd"] = ((unc + wmult * write + READ_MULT * read) / 1e6 * ri
                                    + r["output_tokens"] / 1e6 * ro)
            avail = r["ts_epoch"]
            if hit_entry is not None:
                hit_entry["last"] = now
            if read and sys_live:
                se["last"] = now
            if T >= mn:
                if mode == "blocks":
                    full.append({"prompt": P, "last": now, "avail": avail})
                if S and T * len(S) / n >= mn and not sys_live:
                    sysc[S] = {"last": now, "avail": avail}
    simulate_statectl(rows, order)


def simulate_statectl(rows: list[dict], order: list[int]) -> None:
    """True state control: every agent thread keeps its state server-side (never
    expires).  Turn k re-reads the previous turn's prompt + response as cache and
    writes only the delta; forks (compaction-guidance, hard-stop, gate-rewrite)
    read the parent thread's state.  First turn of a thread reads the system
    prompt if any earlier call of the session used it.  Model minimum applies.
    Text-independent (does not need the transcript to be rendered verbatim)."""
    state: dict[str, int] = {}          # thread -> tokens in cached state (prompt + response)
    sys_seen: set[str] = set()
    for i in order:
        r = rows[i]
        T, S, mn = r["input_tokens"], r["_system"], min_cacheable(r["model"])
        n = max(len(r["_prompt"]), 1)
        ri, ro = price_for(r["model"])
        if r["kind"].endswith("(single-shot)"):
            # policy: no cache breakpoint on one-shot helper calls (no reuse -> no write premium)
            r[f"{STATECTL}_read_tokens"], r[f"{STATECTL}_write_tokens"], r[f"{STATECTL}_uncached_tokens"] = 0, 0, T
            r[f"{STATECTL}_hit"] = ""
            r[f"{STATECTL}_cost_usd"] = T / 1e6 * ri + r["output_tokens"] / 1e6 * ro
            continue
        st = state.get(r["thread"])
        kind = ""
        if st is not None:
            read, kind = min(st, T), "state"
        elif S in sys_seen:
            read, kind = round(T * len(S) / n), "system"
        else:
            read = 0
        if read < mn:
            read, kind = 0, ""
        rest = T - read
        write, unc = (rest, 0) if T >= mn else (0, rest)
        r[f"{STATECTL}_read_tokens"], r[f"{STATECTL}_write_tokens"], r[f"{STATECTL}_uncached_tokens"] = read, write, unc
        r[f"{STATECTL}_hit"] = kind
        r[f"{STATECTL}_cost_usd"] = ((unc + 1.25 * write + READ_MULT * read) / 1e6 * ri
                                    + r["output_tokens"] / 1e6 * ro)
        if S:
            sys_seen.add(S)
        if not r["is_fork"]:
            state[r["thread"]] = T + r["output_tokens"]


def thread_key(r: dict) -> str:
    return r["thread"]


def new_agg() -> dict:
    a = {"calls": 0, "input_tokens": 0, "output_tokens": 0, "actual_usd": 0.0}
    for v in VN:
        a[f"{v}_read"] = a[f"{v}_write"] = a[f"{v}_uncached"] = 0
        a[f"{v}_usd"] = 0.0
    return a


def add(a: dict, r: dict) -> None:
    a["calls"] += 1
    a["input_tokens"] += r["input_tokens"]
    a["output_tokens"] += r["output_tokens"]
    a["actual_usd"] += r["cost_in_usd"] + r["cost_out_usd"]
    for v in VN:
        a[f"{v}_read"] += r[f"{v}_read_tokens"]
        a[f"{v}_write"] += r[f"{v}_write_tokens"]
        a[f"{v}_uncached"] += r[f"{v}_uncached_tokens"]
        a[f"{v}_usd"] += r[f"{v}_cost_usd"]


def merge(a: dict, b: dict) -> None:
    for k, v in b.items():
        a[k] = a.get(k, 0) + v


def fmt_agg(a: dict, keys: dict) -> dict:
    out = dict(keys)
    out.update({"calls": a["calls"], "input_tokens": a["input_tokens"],
                "output_tokens": a["output_tokens"], "cost_actual_usd": round(a["actual_usd"], 4)})
    tin = max(a["input_tokens"], 1)
    for v in VN:
        out[f"cost_{v}_usd"] = round(a[f"{v}_usd"], 4)
        out[f"{v}_saving_pct"] = round((1 - a[f"{v}_usd"] / a["actual_usd"]) * 100, 1) if a["actual_usd"] else ""
        out[f"{v}_read_share"] = round(a[f"{v}_read"] / tin, 4)
        out[f"{v}_write_share"] = round(a[f"{v}_write"] / tin, 4)
        out[f"{v}_uncached_share"] = round(a[f"{v}_uncached"] / tin, 4)
    return out


def run_cache() -> None:
    per_prompt, per_tier, per_kind, threads = [], defaultdict(new_agg), defaultdict(new_agg), []
    kind_counts = defaultdict(lambda: defaultdict(int))
    sessions = collect_sessions()
    for phase, pid, sdir in sessions:
        rows = []
        for cap in sorted(sdir.rglob("anthropic_raw_capture.jsonl")):
            rows.extend(parse_capture_texts(cap, sub_role(cap.parent.relative_to(sdir))))
        simulate_cache(rows)
        a = new_agg()
        by_thread = defaultdict(list)
        for r in rows:
            add(a, r)
            add(per_tier[(phase, r["role"], r["tier"])], r)
            add(per_kind[(phase, r["role"], r["kind"])], r)
            by_thread[thread_key(r)].append(r)
            for v in VN:
                kind_counts[(phase, r["role"], r["kind"], v)][r[f"{v}_hit"] or "miss"] += 1
        for key, trs in by_thread.items():
            trs.sort(key=lambda r: r["ts_epoch"] - r["elapsed_s"])
            gaps = [(b["ts_epoch"] - b["elapsed_s"]) - a_["ts_epoch"] for a_, b in zip(trs, trs[1:])]
            t = new_agg()
            for r in trs:
                add(t, r)
            threads.append({
                "phase": phase, "prompt_id": pid, "session": sdir.name, "thread": key,
                "role": trs[0]["role"], "kind": trs[0]["kind"], "turns": len(trs),
                "forks": sum(r["is_fork"] for r in trs),
                "state_hits_5m": sum(r["cache5m_hit"] == "state" for r in trs),
                "system_hits_5m": sum(r["cache5m_hit"] == "system" for r in trs),
                "state_hits_ideal": sum(r["ideal_hit"] == "state" for r in trs),
                "system_hits_ideal": sum(r["ideal_hit"] == "system" for r in trs),
                "state_hits_statectl": sum(r[f"{STATECTL}_hit"] == "state" for r in trs),
                "median_gap_s": round(statistics.median(gaps), 1) if gaps else "",
                "max_gap_s": round(max(gaps), 1) if gaps else "",
                "gaps_over_300s": sum(g > 300 for g in gaps),
                "input_tokens": t["input_tokens"], "cost_actual_usd": round(t["actual_usd"], 4),
                "cost_cache5m_usd": round(t["cache5m_usd"], 4), "cost_ideal_usd": round(t["ideal_usd"], 4),
                "cost_statectl_usd": round(t[f"{STATECTL}_usd"], 4),
                "ideal_read_share": round(t["ideal_read"] / max(t["input_tokens"], 1), 4),
                "statectl_read_share": round(t[f"{STATECTL}_read"] / max(t["input_tokens"], 1), 4),
            })
        tag = "_".join(sdir.name.split("_")[1:3]) if sdir.name.startswith("run_") else sdir.name
        per_prompt.append({"phase": phase, "prompt_id": pid, "session": sdir.name, "tag": tag, "agg": a,
                           "n_threads": len(by_thread)})
        for r in rows:  # free the texts
            r.pop("_prompt", None); r.pop("_system", None)
        print(f"  {phase:<8} {str(pid):<6} {len(rows):>4} calls  actual=${a['actual_usd']:7.2f}  "
              f"5m=${a['cache5m_usd']:7.2f}  ideal=${a['ideal_usd']:7.2f}  statectl=${a[f'{STATECTL}_usd']:7.2f}  "
              f"read ideal={a['ideal_read'] / max(a['input_tokens'], 1):.2f} "
              f"statectl={a[f'{STATECTL}_read'] / max(a['input_tokens'], 1):.2f}", flush=True)

    latest = {}
    for p in per_prompt:
        k = (p["phase"], p["prompt_id"])
        if k not in latest or p["tag"] > latest[k]:
            latest[k] = p["tag"]
    for p in per_prompt:
        p["superseded"] = latest[(p["phase"], p["prompt_id"])] != p["tag"]

    # per prompt
    with open(OUT / "cache_state_whatif.csv", "w", newline="", encoding="utf-8") as fh:
        rows_out = [fmt_agg(p["agg"], {"phase": p["phase"], "prompt_id": p["prompt_id"], "session": p["session"],
                                       "superseded": p["superseded"], "threads": p["n_threads"]})
                    for p in sorted(per_prompt, key=lambda p: (p["phase"], str(p["prompt_id"])))]
        w = csv.DictWriter(fh, fieldnames=list(rows_out[0])); w.writeheader(); w.writerows(rows_out)

    # per phase x role x call kind (all captured sessions)
    kind_out = []
    for (phase, role, kind), a in sorted(per_kind.items(), key=lambda kv: (kv[0][0], kv[0][1], -kv[1]["actual_usd"])):
        row = fmt_agg(a, {"phase": phase, "role": role, "kind": kind})
        for v in ("cache5m", "ideal", STATECTL):
            kc = kind_counts[(phase, role, kind, v)]
            row[f"{v}_state_hits"], row[f"{v}_system_hits"], row[f"{v}_misses"] = kc["state"], kc["system"], kc["miss"]
        kind_out.append(row)
    with open(OUT / "cache_state_whatif_kinds.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(kind_out[0])); w.writeheader(); w.writerows(kind_out)
    tier_out = [fmt_agg(a, {"phase": phase, "role": role, "tier": tier})
                for (phase, role, tier), a in sorted(per_tier.items())]
    with open(OUT / "cache_state_whatif_tiers.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(tier_out[0])); w.writeheader(); w.writerows(tier_out)
    # benchmark-wide kind rollup (all phases/roles)
    kind_all = defaultdict(new_agg)
    for (phase, role, kind), a in per_kind.items():
        merge(kind_all[kind], a)

    with open(OUT / "cache_state_threads.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(threads[0])); w.writeheader(); w.writerows(threads)

    # scopes
    canon = [p for p in per_prompt if not p["superseded"]]

    def scope(label, ps):
        a = new_agg()
        for p in ps:
            merge(a, p["agg"])
        return fmt_agg(a, {"scope": label, "prompts": len(ps)})

    summary = [scope("Main (captured canonical)", [p for p in canon if p["phase"] == "Main"]),
               scope("Analysis (canonical)", [p for p in canon if p["phase"] == "Analysis"]),
               scope("Query (canonical)", [p for p in canon if p["phase"] == "Query"]),
               scope("ALL captured canonical", canon),
               scope("ALL incl. superseded", per_prompt)]

    # August x4 extrapolation: per-(role,tier) input discount from captured Main sessions
    main_tier = {(ro, t): a for (ph, ro, t), a in per_tier.items() if ph == "Main"}
    main_all = new_agg()
    for a in main_tier.values():
        merge(main_all, a)

    def disc(a, v):
        tin = a["input_tokens"] or 1
        wm = CACHE_VARIANTS[v][1] if v in CACHE_VARIANTS else 1.25
        return (a[f"{v}_uncached"] + wm * a[f"{v}_write"] + READ_MULT * a[f"{v}_read"]) / tin
    est = list(csv.DictReader(open(OUT / "estimated_calls_august.csv", encoding="utf-8")))
    aug = {"scope": "August x4 (EXTRAPOLATED: est. tokens x captured Main per-tier discount)", "prompts": 4,
           "calls": sum(int(e["calls"]) for e in est),
           "input_tokens": sum(int(e["est_input_tokens"]) for e in est),
           "output_tokens": sum(int(e["est_output_tokens"]) for e in est)}
    aug_in = {v: 0.0 for v in VN}
    aug_in_list = aug_out = 0.0
    for e in est:
        ri, ro = price_for(e["model"])
        tin, tout = int(e["est_input_tokens"]), int(e["est_output_tokens"])
        aug_in_list += tin / 1e6 * ri
        aug_out += tout / 1e6 * ro
        a = main_tier.get((e["role"], e["tier"]), main_all)
        for v in VN:
            aug_in[v] += tin / 1e6 * ri * disc(a, v)
    aug["cost_actual_usd"] = round(aug_in_list + aug_out, 4)
    for v in VN:
        aug[f"cost_{v}_usd"] = round(aug_in[v] + aug_out, 4)
        aug[f"{v}_saving_pct"] = round((1 - (aug_in[v] + aug_out) / (aug_in_list + aug_out)) * 100, 1)
    summary.append(aug)
    grand = {"scope": "GRAND canonical (63 captured + 4 extrapolated)", "prompts": 67}
    base = summary[3]
    for k in ("calls", "input_tokens", "output_tokens"):
        grand[k] = base[k] + aug[k]
    grand["cost_actual_usd"] = round(base["cost_actual_usd"] + aug["cost_actual_usd"], 4)
    for v in VN:
        grand[f"cost_{v}_usd"] = round(base[f"cost_{v}_usd"] + aug[f"cost_{v}_usd"], 4)
        grand[f"{v}_saving_pct"] = round((1 - grand[f"cost_{v}_usd"] / grand["cost_actual_usd"]) * 100, 1)
    summary.append(grand)
    cols = list(summary[0])
    with open(OUT / "cache_state_summary.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(summary)

    print("\n== scopes (actual -> cache5m / cache1h / sysonly5m / ideal / statectl) ==")
    for s in summary:
        print(f"{s['scope'][:60]:<60} ${s['cost_actual_usd']:>8.2f} -> "
              + " / ".join(f"${s[f'cost_{v}_usd']:.2f} ({s[f'{v}_saving_pct']:+.1f}%)".replace("+-", "-")
                           for v in VN))
    print("\n== input-token shares (read/write/uncached), captured canonical ==")
    for v in VN:
        print(f"  {v:<10} read={base[f'{v}_read_share']:.3f} write={base[f'{v}_write_share']:.3f} "
              f"uncached={base[f'{v}_uncached_share']:.3f}")
    print("\n== call kinds, benchmark-wide (calls, list cost, share, saving 5m / ideal / statectl, read share statectl) ==")
    tot = sum(a["actual_usd"] for a in kind_all.values())
    for kind, a in sorted(kind_all.items(), key=lambda kv: -kv[1]["actual_usd"]):
        f = fmt_agg(a, {})
        print(f"  {kind:<46} n={a['calls']:>5} ${a['actual_usd']:>7.2f} ({a['actual_usd'] / tot:5.1%})  "
              f"5m {f['cache5m_saving_pct']:>5}%  ideal {f['ideal_saving_pct']:>5}%  statectl {f[f'{STATECTL}_saving_pct']:>5}%  "
              f"read={f[f'{STATECTL}_read_share']:.2f}")
    print("\n== phase x role x kind (calls, actual, saving 5m/ideal/statectl, hits state/system/miss @5m | @statectl) ==")
    for t in kind_out:
        print(f"  {t['phase']:<8} {t['role']:<13} {t['kind'][:40]:<40} n={t['calls']:>5} ${t['cost_actual_usd']:>7.2f} "
              f"{t['cache5m_saving_pct']:>5}% {t['ideal_saving_pct']:>5}% {t[f'{STATECTL}_saving_pct']:>5}%  "
              f"{t['cache5m_state_hits']}/{t['cache5m_system_hits']}/{t['cache5m_misses']} | "
              f"{t[f'{STATECTL}_state_hits']}/{t[f'{STATECTL}_system_hits']}/{t[f'{STATECTL}_misses']}")
    print(f"\noutputs -> {OUT}")


# ════ origin (OriginPro project) ══════════════════════════════════════════════════

# NOTE: .absolute()/literal only -- never .resolve() on N: (UNC -> MAX_PATH).
OPJU = ODIR / "benchmark_cost_layers.opju"
VALIDATION = ODIR / "benchmark_cost_layers_validation.json"

MODE_LABEL = {"sessions": "by subagent sessions", "workers": "by worker layers"}
PANELS = [
    ("Main", "sessions", "MS"), ("Main", "workers", "MW"),
    ("Analysis", "sessions", "AS"), ("Analysis", "workers", "AW"),
    ("Query", "sessions", "QS"), ("Query", "workers", "QW"),
]
FAM_ORDER = {
    "Main": ["1.1", "1.2", "2", "3", "4"],
    "Analysis": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
    "Query": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
}
PHASE_LETTER = {"Main": "M", "Analysis": "A", "Query": "Q"}

SEG_COLOR = {
    "agent itself": "#4c72b0", "query subagents": "#dd8452",
    "analysis subagents": "#55a868", "agent total": "#4c72b0",
    "own L0-main": "#2f4b7c", "own L1-worker": "#6e8fc9", "own misc": "#b9c9e8",
    "q-sub L0-main": "#b35a1f", "q-sub L1-worker": "#e8945a", "q-sub misc": "#f5c9a8",
    "a-sub L0-main": "#2e6b45", "a-sub L1-worker": "#6fb98f", "a-sub misc": "#bfe3cf",
    "L0-main": "#2f4b7c", "L1-worker": "#6e8fc9", "other": "#b9c9e8",
}
STAT_KEYS = ("mean_total", "median", "p10", "p90", "min", "max", "n")


# ── data loading ─────────────────────────────────────────────────────────

def read_wide(phase: str, mode: str):
    path = ODIR / f"layers_wide_{phase}_{mode}_Origin_ready.tsv"
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    header = list(rows[0].keys())
    segs = header[1:header.index("mean_total")]
    fam_seg = {r["family"]: {s: float(r[s]) for s in segs} for r in rows}
    fam_stat = {r["family"]: {k: float(r[k]) for k in STAT_KEYS} for r in rows}
    return segs, fam_seg, fam_stat


def read_totals():
    path = ODIR / "layer_prompt_totals_Origin_ready.tsv"
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    out: dict[str, dict[str, list[tuple[float, bool]]]] = {}
    for r in rows:
        out.setdefault(r["agent"], {}).setdefault(r["family"], []).append(
            (float(r["total_cost_usd"]), r["estimated"] == "True"))
    return out


# ── Origin helpers ───────────────────────────────────────────────────────

def make_app():
    import win32com.client  # type: ignore[import-not-found]  # lazy: OriginPro only
    app = win32com.client.gencache.EnsureDispatch("Origin.Application")
    app.Visible = 0
    return app


def new_book(app, short: str, long_name: str, ncols: int):
    rng = app.CreatePage(2, short, "Origin", 2)
    wks = app.FindWorksheet(rng)
    wks.Execute(f"wks.ncols={ncols};")
    app.ActivePage.LongName = long_name
    return rng, wks


def set_family_x(app, rng, wks, families):
    wks.Execute("wks.col1.type=4;")
    for i, f in enumerate(families, start=1):
        wks.Execute(f'col(1)[{i}]$="{f}";')
    wks.Execute('wks.col1.lname$="family";')


def put_numeric(app, rng, matrix, col_offset):
    if matrix and matrix[0]:
        app.PutWorksheet(rng, matrix, 0, col_offset)


def export_png(app, gname, width=1500):
    app.Execute(f"win -a {gname};")
    app.Execute(f'expGraph type:=png export:=page filename:="{gname}" '
                f'path:="{ODIR}" overwrite:=replace tr1.unit:=2 tr1.width:={width} '
                'tr.Margin:=2;')
    app.Run()


# ── one panel ────────────────────────────────────────────────────────────

def build_panel(app, phase, mode, code, totals):
    segs, fam_seg, fam_stat = read_wide(phase, mode)
    families = [f for f in FAM_ORDER[phase] if f in fam_seg]
    k = len(segs)

    # means reference sheet: family + raw segment means
    mrng, mwks = new_book(app, "M" + code, f"{phase} {mode} - segment means", 1 + k)
    set_family_x(app, mrng, mwks, families)
    for c, s in enumerate(segs, start=2):
        mwks.Execute(f'wks.col{c}.type=1; wks.col{c}.lname$="{s}";')
    put_numeric(app, mrng, [[fam_seg[f][s] for s in segs] for f in families], 1)

    # cumulative plot sheet: columns top-segment-first (tallest cumulative first)
    order = list(range(k - 1, -1, -1))  # seg indices, top first
    crng, cwks = new_book(app, "C" + code, f"{phase} {mode} - cumulative (plot)", 1 + k)
    set_family_x(app, crng, cwks, families)
    for p, j in enumerate(order):
        c = 2 + p
        cwks.Execute(f'wks.col{c}.type=1; wks.col{c}.lname$="{segs[j]}";')
    cmat = [[sum(fam_seg[f][segs[i]] for i in range(j + 1)) for j in order]
            for f in families]
    put_numeric(app, crng, cmat, 1)

    # ---- plot cumulative columns (separate -> overlap), tallest first ----
    gname = "G" + code
    for p in range(k):
        ycol = 2 + p
        if p == 0:
            app.Execute(f"plotxy iy:=[C{code}]1!(1,{ycol}) plot:=203 "
                        f"ogl:=[<new template:=column name:={gname}>];")
        else:
            app.Execute(f"plotxy iy:=[C{code}]1!(1,{ycol}) plot:=203 ogl:=[{gname}]1!;")
    app.Execute(f"win -a {gname};")
    for p, j in enumerate(order, start=1):
        col = SEG_COLOR[segs[j]]
        app.Execute(f'range rr=1!{p}; set rr -cf color("{col}"); set rr -c color("#ffffff");')

    # ---- scatter overlay: per-prompt totals centered on each family ----
    srng, swks = new_book(app, "S" + code, f"{phase} {mode} - prompt totals", 3)
    swks.Execute('wks.col1.type=4; wks.col2.type=1; wks.col3.type=1;'
                 'wks.col1.lname$="fam_idx"; wks.col2.lname$="prompt total (USD)";'
                 'wks.col3.lname$="estimated";')
    srows = []
    for idx, fam in enumerate(families, start=1):
        for tot, est in sorted(totals.get(phase, {}).get(fam, [])):
            srows.append([float(idx), tot, 1.0 if est else 0.0])
    put_numeric(app, srng, srows, 0)
    if srows:
        app.Execute(f"plotxy iy:=[S{code}]1!(1,2) plot:=201 ogl:=[{gname}]1!;")
        # Creating/plotting the scatter book stole focus; reclaim the graph so
        # the symbol, axis, and title commands below hit the right window.
        app.Execute(f"win -a {gname};")
        sp = k + 1
        app.Execute(f'range rs=1!{sp}; set rs -k 2; set rs -z 6; '
                    f'set rs -csf color("#222222"); set rs -cse color("#222222");')

    # ---- axes / titles ----
    app.Execute(f"win -a {gname};")
    app.Execute("layer.y.rescale; layer.y.from=0;")
    app.Execute('yl.text$="cost per prompt (USD)"; xb.text$="family";')
    title = f"{phase} - {MODE_LABEL[mode]}"
    app.Execute(f'label -p 3 92 -j 0 -n Title "{title}"; Title.attach=0; '
                'Title.fsize=14; Title.font=font(Arial); Title.bold=1; '
                'Title.color=color("#202020");')
    app.Execute("doc -uw;")
    return gname, {"segments": segs, "families": families,
                   "n_prompts": {f: int(fam_stat[f]["n"]) for f in families}}


# ── driver ───────────────────────────────────────────────────────────────

def run_origin():
    ODIR.mkdir(parents=True, exist_ok=True)
    totals = read_totals()
    app = make_app()
    meta = {}
    try:
        app.NewProject()
        graphs = []
        for phase, mode, code in PANELS:
            gname, info = build_panel(app, phase, mode, code, totals)
            graphs.append(gname)
            meta[f"{phase}_{mode}"] = info
            export_png(app, gname)
            print(f"built {gname}: {info['segments']}")
        app.Run()
        if not app.Save(str(OPJU)):
            raise RuntimeError(f"Origin failed to save {OPJU}")
        print("saved:", OPJU)
        gcount_before = app.GraphPages.Count
    finally:
        app.Exit()

    # reopen + verify
    app2 = make_app()
    try:
        if not app2.Load(str(OPJU), True):
            raise RuntimeError("reopen failed")
        app2.Run()
        gcount = app2.GraphPages.Count
        wcount = app2.WorksheetPages.Count
        names = sorted(app2.GraphPages.Item(i).Name for i in range(gcount))
    finally:
        app2.Exit()

    record = {
        "status": "validated",
        "opju": str(OPJU),
        "graph_count_before": gcount_before,
        "graph_count_after_reopen": gcount,
        "worksheet_pages_after_reopen": wcount,
        "graph_names": names,
        "panels": meta,
        "opju_bytes": OPJU.stat().st_size if OPJU.exists() else 0,
    }
    VALIDATION.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(json.dumps({k: record[k] for k in
                      ("graph_count_after_reopen", "worksheet_pages_after_reopen",
                       "graph_names", "opju_bytes")}, indent=2))


# ════ command line ═══════════════════════════════════════════════════════════

STEPS = {"audit": run_audit, "layers": run_layers, "cache": run_cache, "origin": run_origin}
DEFAULT_STEPS = ['audit', 'layers', 'cache']


def main(argv: list[str] | None = None) -> None:
    """python {this file} [audit | layers | cache | origin | all] ...  (default: audit layers cache)"""
    args = [a.lower() for a in (sys.argv[1:] if argv is None else argv)] or DEFAULT_STEPS
    if args == ["all"]:
        args = list(STEPS)
    unknown = [a for a in args if a not in STEPS]
    if unknown:
        raise SystemExit(f"unknown step(s) {unknown}; choose from {list(STEPS)} or 'all'")
    for a in args:
        print(f"\n=== {a} ===", flush=True)
        STEPS[a]()


if __name__ == "__main__":
    main()
