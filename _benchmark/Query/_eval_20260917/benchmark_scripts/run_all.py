#!/usr/bin/env python
"""Run/preflight all five arms sequentially, forwarding common CLI options."""

from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SCRIPTS = (
    "run_only_sql_prefixed.py",
    "run_only_sql_no_prefix.py",
    "run_only_sql_rawdb.py",
    "run_bare_model.py",
    "run_flat_tools.py",
)


def main() -> int:
    if any(
        arg == "--output" or arg.startswith("--output=")
        for arg in sys.argv[1:]
    ):
        print(
            "run_all.py does not accept --output because all five arms would "
            "collide. Run individual launchers for output overrides.",
            file=sys.stderr,
        )
        return 2
    for script in SCRIPTS:
        command = [sys.executable, str(HERE / script), *sys.argv[1:]]
        print(f"\n=== {script} ===", flush=True)
        completed = subprocess.run(command, check=False)
        if completed.returncode:
            return completed.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
