# Contributing

Start with the [installation guide](docs/INSTALLATION.md) and
[development guide](docs/DEVELOPMENT.md). The latter maps the modules and lists
local checks that do not require model-provider access.

For a bug report, include the command or browser action, the expected and actual
behavior, the Python version, and the relevant database filenames. For a
scientific result, also include the prompt, model, run directory, and source
identifiers needed to reproduce it. Remove provider credentials from logs before
sharing them.

For a change, describe the resulting behavior and the checks run. Preserve the
sibling browser/project layout, declared `_output` and `_benchmark` locations,
and typed database identifiers. Update the relevant documentation when changing
an entrypoint, output format, or data dependency. Workflow Markdown consumed by
agents is executable configuration and should be reviewed with that effect in
mind.

See the [publication guide](docs/PUBLICATION.md) for preparing a release and its
data bundle.
