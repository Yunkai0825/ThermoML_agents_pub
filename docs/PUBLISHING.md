# Publishing original files

[Documentation home](../README.md)

All published source, databases, and saved outputs retain their original bytes.
Git LFS, Git-annex placeholders, symbolic links, submodules, and download stubs
are prohibited. `.gitattributes` disables content filters and newline conversion.

For this publication, the approved distribution is the Git repository plus
[seven unchanged assets on the `workspace-20260918` release](https://github.com/Yunkai0825/ThermoML_research_agents_pub/releases/tag/workspace-20260918).
Only those seven original files are excluded from Git; they remain part of the
publication. Their exact filenames, local destinations, sizes, and SHA-256 hashes
are recorded in [RELEASE_ASSETS.json](RELEASE_ASSETS.json). The
[installation table](INSTALLATION.md#download-the-release-assets) maps each asset
to its original local path. No placeholder file is committed at those paths.
The two benchmark asset names have Main/Analysis prefixes to prevent release
filename collisions; their bytes are unchanged.

Before publishing, verify every uploaded asset against the manifest. Upload each
original file directly without recompression or content conversion. Keep all
other source, databases, benchmark ZIPs, and shared `_output` artifacts in Git;
`.gitignore` has exact entries for the seven release-asset paths alongside local
generated files and machine settings. Do not expand those asset exclusions or
change the distribution plan without explicit approval.

Hook activation requires an existing Git checkout. For a workspace snapshot
without a `.git` directory, first initialize or restore the intended checkout
as a separate authorized operation. The activation command does not initialize
a repository, stage files, commit, or push:

```shell
python scripts/check_no_pointers.py --install-hook
```

When first adding the hook, preserve its executable bit in Git:

```shell
git add --chmod=+x .githooks/pre-push
```

Check staged files before committing, then check the committed refs before
pushing (replace `HEAD` with the actual refs you will publish):

```shell
python scripts/check_no_pointers.py --staged
python scripts/check_no_pointers.py --refs HEAD
```

The pre-push hook checks every object reachable from the refs being pushed,
including historical commits and annotated tags. It rejects recognized LFS,
Git-fat, and Git-annex pointer files, symbolic links, and submodules even when
the current working copy contains the original file. It reads object metadata
first and inspects only trees and small blobs, so large original database/ZIP
blobs are not loaded for pointer detection. The size bound is 8 KiB, above the
standard Git LFS pointer size; the written policy also forbids other kinds of
placeholder that cannot be identified from a standard signature.

Hooks are local Git configuration and are not automatically enabled by cloning.
Run the activation command in each checkout. Do not use `--no-verify` or otherwise
bypass this policy. Hosting services can impose independent file-size limits;
if a push is rejected, retain the originals and resolve that limit explicitly
instead of converting files to pointers.

The seven release assets exceed [GitHub's 100 MiB ordinary-file limit](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).
Publishing their unchanged bytes as release assets is the approved way to keep
those originals available. It does not authorize pointer substitutes, loss of
files, or replacement of the contents with download instructions.

When updating a repository that already used LFS, a new commit containing original
files still retains pointer blobs in its ancestry. The committed-object check
rejects that history too. The user approved replacing `main` with pointer-free history for the
`workspace-20260918` publication. That authorization covers this replacement;
future remote-history replacements require separate explicit approval. Never
bypass the committed-object check.
