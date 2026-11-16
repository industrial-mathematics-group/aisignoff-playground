# Reference overview

The reference pages list what the repository's configuration and files contain, without background. For the ideas behind them, see the [concepts](../concepts/index.md) section.

## Pages

| Page | What it covers |
|---|---|
| [SIGNOFF.toml reference](signoff-toml.md) | Every key used in `SIGNOFF.toml`: `version`, `exclude`, `[history]`, `[policy]`, `[[annotations]]`, `[[attestations]]` and `[[commits]]`, with this repository's values. |
| [Workflow inputs, triggers and permissions](workflow-options.md) | For each workflow in `.github/workflows/`: triggers, permissions, inputs (`weight`, `aisignoff-version`), environment variables and the `aisignoff` commands it runs. |
| [Repository file reference](repository-files.md) | What each file is and how it is declared: the package in `src/playground`, tests, `scripts/make_results.py`, `results/`, `pyproject.toml`, `.gitignore`, `CITATION.cff` and `zensical.toml`. |

## Where to look

| You want to know | Go to |
|---|---|
| Which keys `SIGNOFF.toml` accepts, and how a value in this repository is set | [SIGNOFF.toml reference](signoff-toml.md) |
| When a workflow runs and what permissions it asks for | [Workflow options](workflow-options.md) |
| Where the aisignoff version is set | [Workflow options](workflow-options.md); for the background, [updating aisignoff](../deploy-extend/updating-aisignoff.md) |
| What a file in the repository is for and which levels it is declared at | [Repository files](repository-files.md) |
| How the documentation site is configured | The `zensical.toml` section of [Repository files](repository-files.md) |

## Related pages

- [Where declarations are kept](../concepts/where-declarations-live.md) explains how annotations, inline tags and commit descriptions combine.
- [The GitHub workflows](../deploy-extend/workflows.md) describes what each workflow does in prose.
- [Troubleshooting](../troubleshooting.md) covers the errors you may see when a configuration value is wrong.
