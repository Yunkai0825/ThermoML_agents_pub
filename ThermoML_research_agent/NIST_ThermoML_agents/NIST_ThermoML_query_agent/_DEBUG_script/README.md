# Debug Scripts

Test runner and prompts for validating the query agent end-to-end.

## Files

| File | Purpose |
|------|---------|
| `run_tests.py` | Unified test runner — sequential (default) or parallel with `ThreadPoolExecutor` + rate limiter |
| `test_prompts.md` | 20 test prompts in 6 categories |

## Test Prompt Categories

| Section | Focus | # Prompts |
|---------|-------|-----------|
| 1 | Basic queries (binary systems, property lookup) | 5 |
| 2 | Intermediate (top-K, property ranking) | 3 |
| 3 | Advanced (cross-property, range, best-DOI) | 3 |
| 4 | Comprehensive (pure compound overview, binary vs ternary) | 2 |
| 5 | Edge cases (unknown compound, out-of-DB property) | 2 |
| 6 | Ternary estimation (DMF/EG + water + co-solvents) | 5 |

## Running Tests

```bash
# All prompts, sequential (--workers 1)
python run_tests.py

# All prompts, parallel with 5 workers and 6s gap (default)
python run_tests.py --workers 5

# Specific prompts
python run_tests.py 1.1 2.1 6.1

# Specific section
python run_tests.py --section 6

# Custom pacing
python run_tests.py --workers 3 --gap 10
```

## Output Structure

Each run creates `_benchmark/Query/test_run_<timestamp>/`:

```
test_run_20260403_145753/
├── Q1.1_result.md         # Cleaned answer + timing (written immediately)
├── Q1.1_history.md        # Full tool trace (written immediately)
├── Q2.1_result.md
├── Q2.1_history.md
├── ...
├── TEST_SUMMARY_*.md      # Final results table with links
├── TEST_TRACE_*.json      # Machine-readable trace
└── working_memories/       # Per-prompt memory snapshots
    ├── memory_1_1.md
    └── ...
```

Real-time output: each prompt writes its `_result.md` and `_history.md`
immediately upon completion, so you can tail results during a long run.
