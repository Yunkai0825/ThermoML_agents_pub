#!/usr/bin/env python3
"""Reject content substitutes in the index or objects reachable from pushed refs.

Only small blobs and tree objects are read. Large original files are retained
without loading their content. No working-tree clean/smudge filters are invoked.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import stat
import subprocess
import sys

MAX_POINTER_BYTES = 8192  # Standard Git LFS pointers are at most 1024 bytes.
POINTER_PREFIXES = (
    b"version https://git-lfs.github.com/spec/v1",
    b"version https://hawser.github.com/spec/v1",
    b"#$# git-fat ",
    b"/annex/objects/",
    b".git/annex/objects/",
)


def git(repo: Path, *args: str, data: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", "-C", os.fspath(repo), *args], input=data,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def pointer_kind(data: bytes) -> bool:
    first = data.removeprefix(b"\xef\xbb\xbf").splitlines()[0:1]
    return bool(first and any(first[0].startswith(prefix) for prefix in POINTER_PREFIXES))


def tree_entries(data: bytes, hash_bytes: int):
    offset = 0
    while offset < len(data):
        space = data.index(b" ", offset)
        nul = data.index(b"\0", space)
        yield data[offset:space], data[space + 1:nul].decode("utf-8", "replace")
        offset = nul + 1 + hash_bytes
    if offset != len(data):
        raise RuntimeError("Malformed Git tree object")


def inspect_objects(repo: Path, names: dict[str, str]) -> tuple[list[str], int]:
    if not names:
        return [], 0
    metadata = git(
        repo, "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
        data="".join(oid + "\n" for oid in names).encode("ascii"),
    )
    candidates = []
    for line in metadata.splitlines():
        parts = line.split()
        if len(parts) != 3 or parts[1] not in (b"blob", b"tree", b"commit", b"tag"):
            raise RuntimeError("Unable to inspect Git object: " + line.decode("ascii", "replace"))
        oid, kind, size = parts[0].decode("ascii"), parts[1], int(parts[2])
        if kind == b"tree" or (kind == b"blob" and size <= MAX_POINTER_BYTES):
            candidates.append((oid, kind, size))

    problems = []
    with subprocess.Popen(
        ["git", "-C", os.fspath(repo), "cat-file", "--batch"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ) as process:
        assert process.stdin is not None and process.stdout is not None
        for oid, kind, expected_size in candidates:
            process.stdin.write((oid + "\n").encode("ascii"))
            process.stdin.flush()
            header = process.stdout.readline().split()
            if len(header) != 3 or header[1] != kind or int(header[2]) != expected_size:
                process.kill()
                raise RuntimeError("Unexpected Git object response for " + oid)
            content = process.stdout.read(expected_size)
            if len(content) != expected_size or process.stdout.read(1) != b"\n":
                process.kill()
                raise RuntimeError("Incomplete Git object response for " + oid)
            label = names[oid] or oid
            if kind == b"blob" and pointer_kind(content):
                problems.append(f"pointer file: {label} (blob {oid})")
            elif kind == b"tree":
                for mode, name in tree_entries(content, len(oid) // 2):
                    if mode in (b"120000", b"160000"):
                        path = (names[oid].rstrip("/") + "/" + name).lstrip("/")
                        substitute = "symbolic link" if mode == b"120000" else "submodule"
                        problems.append(f"{substitute}: {path} (tree {oid})")
        process.stdin.close()
        stderr = process.stderr.read() if process.stderr is not None else b""
        if process.wait():
            raise RuntimeError(stderr.decode("utf-8", "replace"))
    return problems, len(candidates)


def check_refs(repo: Path, refs: list[str]) -> tuple[list[str], int]:
    # Checking all reachable history also covers new branches/initial pushes and
    # pointers removed from the current tree but still included in the push.
    # --stdin avoids command-length limits when many refs are pushed at once.
    result = git(repo, "rev-list", "--objects", "--stdin", data=("\n".join(refs) + "\n").encode())
    names = {}
    for line in result.splitlines():
        oid, _, name = line.partition(b" ")
        names[oid.decode("ascii")] = name.decode("utf-8", "replace")
    return inspect_objects(repo, names)


def check_staged(repo: Path) -> tuple[list[str], int]:
    names, problems = {}, []
    for entry in git(repo, "ls-files", "--stage", "-z").split(b"\0"):
        if not entry:
            continue
        metadata, path = entry.split(b"\t", 1)
        mode, oid, stage = metadata.split()
        label = path.decode("utf-8", "replace")
        if stage != b"0":
            problems.append(f"unmerged index entry: {label}")
        if mode in (b"120000", b"160000"):
            substitute = "symbolic link" if mode == b"120000" else "submodule"
            problems.append(f"{substitute}: {label}")
        elif mode in (b"100644", b"100755"):
            names[oid.decode("ascii")] = label
    object_problems, count = inspect_objects(repo, names)
    return problems + object_problems, count


def refs_from_push(stream) -> list[str]:
    refs = []
    for line in stream:
        parts = line.split()
        if len(parts) != 4:
            raise RuntimeError("Malformed pre-push update: " + line.rstrip())
        oid = parts[1]
        if set(oid) == {"0"}:  # Deleting a remote ref introduces no content.
            continue
        if len(oid) not in (40, 64) or any(c not in "0123456789abcdef" for c in oid):
            raise RuntimeError("Invalid pre-push object ID: " + oid)
        refs.append(oid)
    return list(dict.fromkeys(refs))


def install_hook(repo: Path) -> None:
    required = (repo / ".githooks/pre-push", repo / "scripts/check_no_pointers.py")
    if not all(path.is_file() for path in required):
        raise RuntimeError("This checkout does not contain the versioned publication hook and checker")
    previous = subprocess.run(
        ["git", "-C", os.fspath(repo), "config", "--get", "core.hooksPath"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if previous.returncode not in (0, 1):
        raise RuntimeError(previous.stderr.decode("utf-8", "replace"))
    current = previous.stdout.decode("utf-8", "replace").strip()
    if current and current != ".githooks":
        raise RuntimeError(f"Existing core.hooksPath is {current!r}; integrate the check there before changing it")
    required[0].chmod(required[0].stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    git(repo, "config", "--local", "core.hooksPath", ".githooks")
    print("Enabled .githooks/pre-push for this checkout. No files were staged or committed.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--staged", action="store_true")
    modes.add_argument("--refs", nargs="+")
    modes.add_argument("--pre-push", action="store_true")
    modes.add_argument("--install-hook", action="store_true")
    args = parser.parse_args(argv)
    try:
        repo = Path(git(args.repo, "rev-parse", "--show-toplevel").decode("utf-8").strip())
        if args.install_hook:
            install_hook(repo)
            return 0
        if args.staged:
            problems, count = check_staged(repo)
        else:
            refs = refs_from_push(sys.stdin) if args.pre_push else args.refs
            problems, count = check_refs(repo, refs) if refs else ([], 0)
        if problems:
            print("NO POINTERS: publication blocked. Restore original files; do not bypass this check.", file=sys.stderr)
            for problem in sorted(set(problems)):
                print("  " + problem, file=sys.stderr)
            return 1
        print(f"No pointer substitutes found ({count} small blobs/tree objects inspected; large blobs kept as-is).")
        return 0
    except (OSError, RuntimeError, ValueError) as exc:
        print("No-pointer check failed: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
